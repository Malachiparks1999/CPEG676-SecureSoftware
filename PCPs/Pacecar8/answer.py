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
Assignment:     Pacecar Problem 9
File Description:  Used to print to the nc session

165.22.46.243", 13337

Run in interactive python to key flag
'''

from pwn import *
p=remote("165.22.46.243", 7331)
print("""scouting tells us expected output looks like:\n
  This isn't vulnerable\n
  This might help 0xffbeea50\n""")
resp=p.recvuntil("help ")
leak=p.recvuntil("\n")
#leak looks like "0xffbeea50\n"
intleak = int(leak,16)
p.sendline("payloadhere")#for nice unprintable payloads
p.interactive()
#if you have a shell then you can now type `ls` and `cat flag`