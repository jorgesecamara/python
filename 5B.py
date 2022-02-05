#Dados números inteiros positivos n, i e j, listar os n primeiros inteiros não-negativos que são múltiplos de i ou de j. Exiba os números numa só linha (ou seja, sem quebra de linha entre os números adjacentes).
#Por exemplo, dados n=6, i=2 e j=3 exibir
#0   2   3   4   6   8

n = int(input("Digite n: "))
i = int(input("Digite i: "))
j = int(input("Digite j: "))

mult = 0 
k = 0
while k < n:
    if mult%i == 0 or mult%j == 0:
        print(mult)
        k = k + 1; 
    mult = mult + 1 
    