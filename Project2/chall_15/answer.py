'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_15
File Description:  Shellcode from NX disabled

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX disabled   PIE enabled     No RPATH   No RUNPATH   69) Symbols       No    0               2               chall_15

File info:
chall_15: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=132611036b789092b3e5c7acb2673007d7afd5b3, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Symbols:
    No win func so going to need to pop a shell
    Going to use printf or puts

Strings:
    Sometimes the canary is in the coal mine, sometimes the canary is on the stack, and sometimes ... baked beans --- only string in binary

Vulns:
    Stack Canary is disabled along with NX so I smell shellcode!
    asm(shellcraft.asm)
    Set context to amd64
'''

# Import Libraries
from pwn import *