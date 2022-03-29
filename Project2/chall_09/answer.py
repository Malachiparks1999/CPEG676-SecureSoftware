'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_09
File Description:  Reversing problem to figure out what X'ORd to pop win func

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   71) Symbols       No    0               1               chall_09

File info:
chall_09: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1b2f0f15e28d4f474e1276b701142231cd1068bd, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Symbols:
rabin2 -s chall_09
    intersting symbol named key, going to see if i can leak
'''

# Import Libaries
from pwn import *

# Making copy of executable format!
elf = ELF("./chall_09", checksec=False)

# Start process
p=process("./chall_09")

# Grab key that is being xor'd
key = elf.sym.key
Hkey = hex(key)
print("Hex Key: ",Hkey)

# Xoring key with 30 to encrpyt
endByte = b"\x30"
Xkey = xor(elf.string(key),endByte)

# Sending and see what happens
p.send(Xkey)
p.interactive()