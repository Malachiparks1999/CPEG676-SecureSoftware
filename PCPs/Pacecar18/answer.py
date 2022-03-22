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