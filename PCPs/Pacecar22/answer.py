'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP22: Clone Wars
File Description:  House of Force on a Starwars Binary

Checksec info:
 RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   83) Symbols       No    0               4               CloneWarS

File info:
CloneWarS: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=a45e46d5347deb6022d64604638a3ed70e8de417, not stripped
'''

# Import Libraries
from pwn import *

