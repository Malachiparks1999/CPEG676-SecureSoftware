;;  Creators:       Malachi Parks
;;  Section:        CPEG476-010
;;  Assignment:     Project 1
;;  File Description:  64 bit assembly that prints a few messages and does a few math operations

;; Compiling instructions
;; nasm -f elf64 MParks_64bit.asm   
;; ld -o MParks_64bit MParks_64bit.o

section .text:
  global _start

sub:
  ;; creating a new stack
  push rbp
  mov rbp, rsp
  ;; room for new variables carried in
  sub rsp, 0x10
  mov [rbp-8], rdi
  mov [rbp-16], rsi
  ;; random subtraction, results in print being called
  mov rax, 127
  sub rax, [rbp-16]
  sub rax, [rbp-8]
  ;; system call to print out message, eax already ready to write out
  xor rdi, rdi    ;; zero out in case of extra junk
  xor rsi, rsi    ;; zero out in case of extra junk
  mov rdi, 1      ;; fd to stdout
  mov rsi, msg    ;; load out message to print
  mov rdx, 99      ;; length of message
  syscall
  ;; system call to print sub message
  xor rdi, rdi    ;; zero out in case of extra junk
  xor rsi, rsi    ;; zero out in case of extra junk
  xor rdx, rdx	  ;; zero out in case of extra junk
  mov rdi, 1      ;; fd to stdout
  mov rsi, subMsg    ;; load out message to print
  mov rdx, 60      ;; length of message
  syscall
  leave
  ret

_start:
  ;; new stack frame
  push rbp
  mov rbp, rsp
  ;; moving variables to be used by sub
  mov rsi, 26
  mov rdi, 100
  call sub
  xor rdi,rdi
  mov rax, 60
  syscall

section	.data ;;0xA and 0xD are new line and then carriage return (enter)
  msg: db 'I will be doing some simple math today!', 0xA, 0xD ;; will be using this to show whats happening
  subMsg: db 'This was called due to subtractions occuring in registers!, 0xA, 0xD' ;; will be used after subtraction occurs
