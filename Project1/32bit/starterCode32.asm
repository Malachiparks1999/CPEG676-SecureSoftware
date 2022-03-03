section .text:
  global _start ;;to compile nasm -f elf t32.asm THEN ld -m elf_i386 -s -o run32 t32.o

util:
  push ebp
  mov ebp, esp
  sub esp, 0x10
  mov dword [esp], 0xdeadbeef
  leave
  ret

_start:
  push ebp
  mov ebp, esp
  call util
  xor ebx,ebx
  mov eax, 0x01
  int 0x80
