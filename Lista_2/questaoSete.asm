.text
	.globl main

	main :

	lw $t0,32($s3) # $t0 recebe A[8]
	add $t0,$s2,$t0 # $t0 recebe h + A[8]
	  sw $t0,48($s3) # armazena o resultado em A[12]

