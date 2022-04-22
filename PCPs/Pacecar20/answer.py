'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP20: ov3flow
File Description:  Baby heap overflow exploit

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   69) Symbols       No    0               2               ov3flow

File info:
ov3flow: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=b5c23ba388e1f233bdc72e9e5570a437c7743500, for GNU/Linux 3.2.0, not stripped

'''

# Import Libraries
from pwn import *

# Can't get to run, want to overflow heap but unsure of what glibc is required