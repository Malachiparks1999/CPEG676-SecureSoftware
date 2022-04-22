'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP19: Naughty
File Description:  sing .fini_array similar to GOT exploit to call system

Checksec info:
    Arch:     i386-32-little
    RELRO:    No RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)

    Interesting, no PIE and is 32bit

File info:
naughty: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter 
/lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=c1f697613751decab2357b9854929211627742a8, not stripped

    I like dynamically linked, means it links everyting via lazy linking
    
Radare2:
afl --> list all functions

Useful Funcs

'''

# Import Libaries
from pwn import *

# set context for auto-pwner
context(arch="i386")
bin=ELF('./naughty')
libc=ELF('libc-2.27.so')

# Starting process
p=process("./naughty")