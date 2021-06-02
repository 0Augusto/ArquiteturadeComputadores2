.text
	.globl main
	
	main:

	addi $s1, $0, 10 # $s1 = 10
	addi $s2, $0, -1 # $s2 = -1

	addi $s1, $s1, 1 # $s1 = $s1 + 1
	add $s3, $s1, $s2 # $s3 = $s1 + $s2

