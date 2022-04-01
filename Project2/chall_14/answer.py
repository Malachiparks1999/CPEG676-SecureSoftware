'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_14
File Description:  

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   Canary found      NX enabled    No PIE          No RPATH   No RUNPATH   1872) Symbols     No    0               0               chall_14

File info:
chall_14: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, BuildID[sha1]=409afffbc385d1f298454dd3044229b712fa15f9, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Symbols:
    So many symbols literally from statically linking this mofo

Strings:


Vulns:
    Statically linked.... I can call whatever I want!
    Not a printf sice tried %p and no return, probably can ret, but also can find a canary
'''

# Import library functions