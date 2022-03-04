'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_06
File Description:  

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX disabled   PIE enabled     No RPATH   No RUNPATH   69) Symbols       No    0               3               chall_06

File info:
chall_06: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=bb31d22b0c8dc2f0dd7a39ca45ef6f9588034ab9, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions
'''