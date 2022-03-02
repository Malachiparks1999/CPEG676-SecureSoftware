;;  Creators:       Malachi Parks
;;  Section:        CPEG476-010
;;  Assignment:     Project 1
;;  File Description:  Used to print to the nc session

;; Compiling instructions
;; nasm -f elf MParks_32bit.asm 
;; ld -m elf_i386 -s -o MParks_32bit MParks_32bit.o

section .text:
  global _start ;; tells the linker where to start

util:
  ;; this line and above set up new stack frame
  push ebp
  mov ebp, esp

  ;; System call to print out to stdout my msg
  sub esp, 41   ;; where message is stored
  mov dword [esp], msg  ;; load in message
  mov edx, 41   ;; msg length
  mov ecx, [ebp-41]  ;; load in message
  mov ebx, 1    ;; write to stdout (file descripter 1)
  mov eax, 4    ;; call sys_write
  int 0x80      ;; sys_call

  ;; print out multiplication message
  sub esp, 23
  mov dword [esp], mul  ;; load in message
  mov edx, 23   ;; msg length
  mov ecx, [ebp-64]  ;; load in message
  mov ebx, 1    ;; write to stdout (file descripter 1)
  mov eax, 4    ;; call sys_write
  int 0x80      ;; sys_call

  ;; Variables for for printing
  sub esp, 4
  mov dword [ebp-68], 11    ;; first num to multiply
  imul ecx, [ebp-68], 7    ;; literal number 77
  sub ecx, 22

  ;; print out multiplication result
  mov edx, 10   ;; msg length\
  mov ebx, 1    ;; write to stdout (file descripter 1)
  mov eax, 4    ;; call sys_write
  int 0x80      ;; sys_call
  leave
  ret

_start:
  push ebp
  mov ebp, esp
  call util   ;; push eip here
  xor ebx,ebx     ;; system call arg1
  mov eax, 0x01   ;; system call arg number
  int 0x80        ;; system call interupt

section	.data ;;0xA and 0xD are new line and then carriage return (enter)
  msg: db 'I will be doing some simple math today!', 0xA, 0xD ;; will be using this to show whats happening
  mul: db 'Multiplying 7 * 11: 77', 0xA, 0xD ;; will be used in showing multiplication