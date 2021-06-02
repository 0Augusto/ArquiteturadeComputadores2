print("Programa em python para calcular o exercicio 30 da lista.")

print("Henrique Augusto Rodrigues")
print("675263")
print("Arquitetura de Computador II")
print("Professor: Romanelli Lodron Zuim")
print()#pular uma linha
#Funcoes do programa
def menu_func():
	print("""Exercicio 30
		Opções:
		(1) = Qual o CPI médio da máquina?
		(2) = Suponha um Overclock de 12/100. Qual o speedUp sobre a máquina original?
		(3) = Suponha uma alteração no Hardware e no acesso à memória. Essa alteração reduz em dois ciclos as instruções da ALU ao custo de aumentar em 1 ciclo os acessos à memória. Qual o speedup sobre a máquina original?
		(4) = Considere um novo compilador que reduza em 50% as instruções da ALU. Qual o speedup sobre a máquina original?
		(5) = Qual o speedup sobre a máq. original se aplicarmos todas as alterações.
		(6) = Qual o tempo de execução de cada benchmark e para cada alteração acima para um código com 10000 instruções.
		(0) = Encerra o programa.
  	""")
menu_func()
print()
escolha = input("Make a wise choice! Escolha o exercicio: ")
#Condicoes das funcoes
if escolha == "0":
	print("Programa encerrado com sucesso! ")
	exit()
#==========================letra a========================================	
elif escolha == "1":
	
		A = float(input("Insira a porcentagem das instrucoes da ALU: "))
		B = float(input("Insira a porcentagem das instrucoes de desvio: "))
		C = float(input("Insira a porcentagem das instrucoes de acesso a memoria: "))
		D = float(input("Insira a porcentagem dos outros: "))

		E = int(input("ALU")) #instrucoes da ALU
		F = int(input("Desvio")) #instrucoes de desvio
		G = int(input("Acesso memoria")) #instrucoes de acesso a memoria
		H = int(input("Outras")) #outras

		CPIMedio = (A * E) + (B * F) + (C * G) + (D * G)

		print("O CPI medio eh: %0.4f" %CPIMedio)
	
#==========================letra b========================================	
elif escolha == "2":
    print("Inserir os número sem a notacao cientifica, dessa forma -> 1 MHZ = 1000000")

    #CPUTimeOriginal = float(input("Insira o CPU original da maquina: "))
    #CPUTimeMelhoria = float(input("Insira o valor melhorado do CPUTIME: "))
    #speedUp = CPUTimeOriginal/CPUTtimeMelhoria

    #ICoriginal = float(input("Insira a instrucao original(IC):" ))
    #CPIorigina = float(input("Insira o CPI original: "))
    f = float(input("Insira a frequencia original(f): "))
    #ICb = float(input("Insira a instrucao de b(ICb): "))
    #CPIb = float(input("Insira o CPI de b: "))
    fb = float(input("Insira a frequencia de b: "))
        
    speedUp = (f ** -1) * (1.12 * fb)
    
    print("O valor do speedup eh: %0.4f" %speedUp)
#==========================letra c========================================
elif escolha == "3":
    A = float(input("Insira a porcentagem da ULA: "))
    B = float(input("Insira a porcentagem das instrucoes de desvio: "))
    C = float(input("Insira a porcentagem das instrucoes de acesso: "))
    D = float(input("Insira a porcentagem das outras: "))
    CPIMedioc = (A * 2) + (B * 3) + (C * 6) + (D * 6)
    print("O CPI medio eh: %0.4f" %CPIMedioc)

    CPIOriginal = float(input("Insira o CPI original (letr a): "))
    speedUpc = CPIOriginal/CPIMedioc
    print("O speedup de c eh: %0.4f" %speedUpc)
#==========================letra d========================================
elif escolha == "4":
    A = int(input("Insira a nova procentagem(metade) da ALU: "))
    B = int(input("Insira a porcentagem (inicial) da instrucao de desvio: "))
    C = int(input("Insira a porcentagem das instrucoes de acesso: "))
    D = int(input("Insira a porcentagem das outras: "))
    qtd = int(input("Insira a nova quantidade de instrucoes: "))
	
    CPIMediod = ((A * 4) + (B * 3) + (C * 5) + (D * 6))/qtd

    print("CPIMediod = %0.4f" %CPIMediod)
    ICori = float(input("Insira a qtd de instrucoes original: "))
    CPIori = float(input("Insira o CPI original: "))
    ICd = float(input("Insira a qtd de instrucoes nova: "))
    CPId = float(input("Insira o CPI nova: "))
    speedUp = (ICori * CPIori)/(ICd * CPId)
    print("O speedup eh: %0.4f" %speedUp)  
#==========================letra e========================================
elif escolha == "5":
    A = float(input("Insira a metade da procentagem da ALU: "))
    B = float(input("Insira a % das instrucoes de desvio: "))
    C = float(input("Insira a % das instrucoes de acesso: "))
    D = float(input("Insira a % das outras: "))
    qtd = int(input("Insiraa a nova quantidade de instrucoes total: "))
     
    CPIe = ((A * 2) + (B * 3) + (C * 6) + (D * 6))/qtd
    print("O valor do CPIe eh: %0.4f" %CPIe)
    ICoriginal = 100
    CPIoriginal = 4.1
    qtd = int(input("Insiraa a nova quantidade de instrucoes total: "))
    speedUp = ((ICoriginal/qtd) * (CPIoriginal/CPIe) * (112/100))
    print("O speedUp atual eh: %0.4f" %speedUp)
#==========================letra f========================================
elif escolha == "6":
	print("6 ok")


