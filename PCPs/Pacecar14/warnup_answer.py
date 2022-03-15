'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP14: Warmup
File Description:  Using printf to leak canary then smash

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   74) Symbols       No    0               3               warmup

File info:
warmup: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=8b72f0fc93f73d288141b26ac556a79cc1c3f495, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions
'''

# Import Libarries
from pwn import *