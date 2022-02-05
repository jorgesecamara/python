#Dizemos que um número inteiro positivo é triangular se ele é o produto de três numeros inteiros consecutivos. 

#Por exemplo, 120 é triangular, pois 4 * 5 * 6 = 120.

#Dado um número inteiro positivo n, exiba a string "sim" se n for triangular e "nao" caso contrário.

n = int(input("Digite o valor de n: "))
i = 3
a = 0
# modifique a condicao na linha abaixo
while a < n:
    a = i*(i-1)*(i-2)
    i += 1
    
if a == n:
    print(i-1, i-2, i-3)
    print("sim")
else:
    print("nao")


# exibir "sim" se for triangular,
# "nao" caso contrario