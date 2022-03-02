;;  Creators:       Malachi Parks
;;  Section:        CPEG476-010
;;  Assignment:     Project 1
;;  File Description:  Used to print to the nc session

section .text:
  global _start ;;to compile nasm -f elf t32.asm THEN ld -m elf_i386 -s -o run32 t32.o

util:
  push ebp
  mov ebp, esp    ;; this line and above set up new stack frame
  sub esp, 0x10
  mov dword [esp], 0xdeadbeef
  leave
  ret

_start:
  push ebp
  mov ebp, esp
  call util   ;; push eip here
  xor ebx,ebx     ;; system call arg1
  mov eax, 0x01   ;; system call arg number
  int 0x80        ;; system call interupt

section	.data
  msg: db 'I will be doing some simple math today!', 39 ;; will be using this to show whats happening