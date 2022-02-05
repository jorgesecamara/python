#Dados um inteiro n > 0 e uma sequência de n números inteiros, determinar o comprimento da maior subsequência crescente.

#Exemplos:

#    Para a sequência 5, 10, 3,  2, 4, 7, 9, 8, 5 retornar 4 
#    Para a sequência 10, 8, 7, 5, 1, 2 retornar 2

n = int(input("Digite n: "))
anterior = int(input("Numero: "))
comprimento = 1
list = [anterior]
list2 = []
n = n - 1
while n > 0:
    n -= 1
    atual = int( input("Numero: "))
    list.append(atual)
    if atual > anterior:
        comprimento += 1
        list2.append(comprimento)
    else:
        comprimento = 1
    anterior = atual
    
#5print(f'para lista de valores {list}', end=' ')
print(max(list2))
