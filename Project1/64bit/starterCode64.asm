section .text: ;;to compile nasm -f elf64 test.asm THEN ld -o runme test.o
  global _start

util:
  push rbp
  mov rbp, rsp
  sub rsp, 0x10
  mov dword [rsp], 0xdeadbeef
  leave
  ret

_start:
  push rbp
  mov rbp, rsp
  call util
  xor rdi,rdi
  mov rax, 0x3c
  syscall