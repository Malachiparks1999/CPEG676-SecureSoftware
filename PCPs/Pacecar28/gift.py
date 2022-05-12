from pwn import *
context.terminal = ['tmux', 'splitw', '-h']
p=process("./a.out")
gdb.attach(p)

def malloc(ind, size, payload):
    global p
    r1 = p.sendlineafter(b">", "1")
    r2 = p.sendlineafter(b">", str(ind))
    r3 = p.sendlineafter(b">", str(size))
    r4 = p.sendlineafter(b">",payload)
    return r1+r2+r3+r4

def free(ind):
    global p
    r1 = p.sendlineafter(b">", "2")
    r2 = p.sendlineafter(b">", str(ind))
    return r1 + r2

def edit(ind, payload):
    global p
    r1 = p.sendlineafter(b">","3")
    r2 = p.sendlineafter(b">",str(ind))
    r3 = p.sendlineafter(b">",payload)
    return r1+r2+r3

def view(ind):
    global p
    r1 = p.sendlineafter(b">", "4")
    r2 = p.sendlineafter(b">", str(ind))
    leak = p.recvuntil(b"addresses.");
    return leak