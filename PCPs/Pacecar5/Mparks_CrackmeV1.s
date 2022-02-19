	.file	"Mparks_CrackmeV1.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"Enter the secret:"
.LC1:
	.string	"%s"
.LC2:
	.string	"That's not the secret!"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB22:
	.cfi_startproc
	pushq	%rbx
	.cfi_def_cfa_offset 16
	.cfi_offset 3, -16
	leaq	.LC0(%rip), %rdi
	subq	$64, %rsp
	.cfi_def_cfa_offset 80
	call	puts@PLT
	movq	%rsp, %rbx
	leaq	.LC1(%rip), %rdi
	xorl	%eax, %eax
	movq	%rbx, %rsi
	call	__isoc99_scanf@PLT
	xorl	%esi, %esi
	movl	$1, %r8d
	xorl	%edx, %edx
	movl	$1, %edi
	leaq	32(%rsp), %r9
	.p2align 4,,10
	.p2align 3
.L2:
	movl	%edx, %ecx
	movl	%edx, %eax
	imulq	$33818641, %rcx, %rcx
	shrq	$32, %rcx
	subl	%ecx, %eax
	shrl	%eax
	addl	%ecx, %eax
	shrl	$6, %eax
	movl	%eax, %ecx
	sall	$7, %ecx
	subl	%eax, %ecx
	movl	%r8d, %eax
	addl	%edi, %r8d
	subl	%ecx, %edx
	xorb	(%rbx,%rsi), %dl
	movb	%dl, (%r9,%rsi)
	addq	$1, %rsi
	movl	%edi, %edx
	movl	%eax, %edi
	cmpq	$20, %rsi
	jne	.L2
	leaq	.LC2(%rip), %rdi
	call	puts@PLT
	addq	$64, %rsp
	.cfi_def_cfa_offset 16
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE22:
	.size	main, .-main
	.ident	"GCC: (Debian 11.2.0-10) 11.2.0"
	.section	.note.GNU-stack,"",@progbits
