.text
	.globl main

	main :

	ori $s1, $0, 0x30541
	sll $s1, $s1, 17
	ori $s2, $0, 9896
	add $s3, $s1, $s2

