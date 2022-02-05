#Escreva um programa que recebe dois inteiros representando o dia  e  mes e exibe#
#
#    1 se a data dia/mês cair no primavera
#    2 se a data dia/mês cair no verão
#    3 se a data dia/mês cair no outono
#    4 se a data dia/mês cair no inverno
#Para fins desse exercício, assuma que a primavera inicia em 22/9, o verão em 21/12, o outono em 20/3 e o inverno em 20/6.
#Exemplos:
#    dia = 12, mes = 2, saída: 2
#    dia = 22, d = 7, saída: 4

dia = int(input("Dia: "))
mes = int(input("Mes: "))
primavera = 1
verao     = 2
outono    = 3
inverno   = 4
if dia >= 22 and mes == 9 or 10 <= mes <= 11 or dia < 21 and mes == 12:
    print(1)
elif dia >= 21 and mes == 12 or 1 <= mes <= 2 or dia < 20 and mes == 3:
    print(2)
elif dia >= 20 and mes == 3 or 4 <= mes <= 5 or dia < 20 and mes == 6:
    print(3)
elif dia >= 20 and mes == 6 or 7 <= mes <= 8 or dia < 22 and mes == 9:
    print(4)
    
#if dia >= 22 and mes >=9
#    print(primavera)
    
#1 = data/mes cair primavera
#2 = data/mes cair verao
#3 = data/mes cair outono 
#4 = data/mes cair inverno 


# assumir primavera = 22/9; verao = 21/12; outono = 20/3; inverno 20/6
