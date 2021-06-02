# Computa os primeiros 20 numerous da serie Fibonacci e coloca em um array, então imprime
      .data
fibs: .word   0 : 12        # "array" de 12 words para conter os valores de fib
size: .word  12             # tamanho "array" 
      .text
      la   $t0, fibs        # load address do array
      la   $t5, size        # load address do tamanho da variavel
      lw   $t5, 0($t5)      # load tamanho do array 
      li   $t2, 1           # 1 eh o primeiro e o segundo numero de  Fib. 
      add.d $f0, $f2, $f4
      sw   $t2, 0($t0)      # F[0] = 1
      sw   $t2, 4($t0)      # F[1] = F[0] = 1
      addi $t1, $t5, -2     # Contador para o  loop, executará (size-2) vezes
loop: lw   $t3, 0($t0)      # Pega o valor do array F[n] 
      lw   $t4, 4($t0)      # Pega o valor do array F[n+1]
      add  $t2, $t3, $t4    # $t2 = F[n] + F[n+1]
      sw   $t2, 8($t0)      # Store F[n+2] = F[n] + F[n+1] in array
      addi $t0, $t0, 4      # incrementa o  endereço da sequencia Fib. da fonte
      addi $t1, $t1, -1     # decrementa loop contador
      bgtz $t1, loop        # Repete se ainda não acabou.
      la   $a0, fibs        # primeiro argumento para print (array)
      add  $a1, $zero, $t5  # segundo argumento para print  (tamanho)
      jal  print            # chama print routine. 
      li   $v0, 10          # chamada do sistema para saída 
      syscall               # saímos todos daqui.
		
#########  routine to print os números em uma linha

      .data
space:.asciiz  " "          # espaço inserido entre os números
head: .asciiz  "Os numeros Fibonacci sao:\n"
      .text
print:add  $t0, $zero, $a0  # inicia address do array
      add  $t1, $zero, $a1  # inicia o contador loop para o tamanho do array
      la   $a0, head        # load address of print heading
      li   $v0, 4           # specify Print String service
      syscall               # print heading
out:  lw   $a0, 0($t0)      # load numero de fibonacci para syscall
      li   $v0, 1           # especifica Print Integer service
      syscall               # imprime numero de fibonacci 
      la   $a0, space       # load address of spacer for syscall
      li   $v0, 4           # specify Print String service
      syscall               # output string
      addi $t0, $t0, 4      # incrementa address
      addi $t1, $t1, -1     # decrementa loop counter
      bgtz $t1, out         # repete se nao acabou
      jr   $ra              # retorna
	
