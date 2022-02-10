	.file	"PCP3.c"
	.intel_syntax noprefix
	.text
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	endbr64
	xor	eax, eax
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.text
	.p2align 4
	.globl	modulus
	.type	modulus, @function
modulus:
.LFB1:
	.cfi_startproc
	endbr64
	mov	eax, edi
	cdq
	idiv	esi
	mov	eax, edx
	ret
	.cfi_endproc
.LFE1:
	.size	modulus, .-modulus
	.p2align 4
	.globl	mod13
	.type	mod13, @function
mod13:
.LFB2:
	.cfi_startproc
	endbr64
	movsx	rax, edi
	mov	edx, edi
	imul	rax, rax, 1321528399
	sar	edx, 31
	sar	rax, 34
	sub	eax, edx
	lea	edx, [rax+rax*2]
	lea	eax, [rax+rdx*4]
	sub	edi, eax
	mov	eax, edi
	ret
	.cfi_endproc
.LFE2:
	.size	mod13, .-mod13
	.p2align 4
	.globl	mod64
	.type	mod64, @function
mod64:
.LFB3:
	.cfi_startproc
	endbr64
	mov	edx, edi
	sar	edx, 31
	shr	edx, 26
	lea	eax, [rdi+rdx]
	and	eax, 63
	sub	eax, edx
	ret
	.cfi_endproc
.LFE3:
	.size	mod64, .-mod64
	.ident	"GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
