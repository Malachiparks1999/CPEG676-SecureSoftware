'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_10
File Description:  

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   71) Symbols       No    0               1               chall_10

File info:
chall_10: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=32fabeea7a1c3e6481f2efcf2c37fa1d6c3255ab, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Vulns:
    Not shell code since NX is on, but no canary or PIE?
    Also printf so maybe a printf vuln ---> tried, does not work so maybe stack smashing?
'''

# Import Libaries
from pwn import *

