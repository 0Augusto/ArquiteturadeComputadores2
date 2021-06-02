.text
	.globl main

	main :
	
	addi $s1, $0, 3 # $s1 = 3
	addi $t0, $0, 4
	div $s1, $t0 # 3/4 — hi — resto (parte alta) e lo — quociente (parte baixa)

