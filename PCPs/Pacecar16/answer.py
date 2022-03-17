'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP16: 
File Description:  

Checksec info:
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   70) Symbols       No    0               2               formatz


File info:
formatz: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=05a675d5e3199650c2d6eead61f1be6a3aa56f66, for GNU/Linux 3.2.0, not stripped


Radare2:
afl --> list all functions

nc 165.22.46.243 8877
'''

# Import Libraries
from pwn import *

# Setup - External
HOST = "165.22.46.243"
PORT = 8877

# Used to get 
print("ELF OF BINARY:")
elf = ELF("./formatz")

# Knows the context to debug in
context.binary = elf
context.log_level = "debug"

def progEnv():
    libc = ELF('/usr/lib64/ld-linux-x86-64.so.2')      # Use local libc library
    return process(elf.path)                # Start a process to use
    '''     COMMENTED OUT FOR NOW TO TEST LOCALLY
    if args.LOCAL:
        libc = ELF('/usr/lib/libc-2.33.so', checksec=False)
        return process([elf.path])
    else:
        libc = ELF('./libc6_2.31-0ubuntu9.2_amd64.so', checksec=False)
        return remote(HOST, PORT), libc
    '''

# Used by the autopwner as a callback function
def exec_fmt(payload):
    p = process([elf.path])
    p.sendline(payload)
    return p.recvall()

def main():
    print("hello!")
    test = progEnv()

# Execute the function main when written
if __name__ == "__main__":
    main()