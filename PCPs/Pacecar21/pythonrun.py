'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP21
File Description:  Used to prove that running heap problem via python

Checksec info:

File info:

'''

# Import libraries 
from pwn import *

# Start proecess will fail
# p=process("./a.out")
# print(p.recv())

# Start process will start
p=process("./a.out", env = {'LD_LIBRARY_PATH' : '.'})
print(p.recv())