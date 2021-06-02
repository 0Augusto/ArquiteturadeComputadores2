.text
	.globl main
	
	main:

	addi $s1, $0, 3 # $s1 = 3
	sll $s2, $0, 10 # $s2 = 3 * 1024

	
	add $s2, $s2, $s1 #$s2 = 1024 * 3 + 3

