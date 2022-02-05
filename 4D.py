#Dados um número inteiro n > 0 e um dígito d tal que 0 <= d <= 9, determinar quantas vezes d ocorre em n.

#Exemplos:

#    n = 63543, d = 3, saída: 2
#    n = 110, d = 0, saída: 1
#    n = 0110, d = 0, saída: 1 (zeros à esquerda não importam)

n = int(input("n: "))
d = int(input("d: "))    # 0 <= d <= 9   ou seja d = [entre 0-9]

#quantas vezes ocorre d em n
#n = d + n

num = n
cont = 0
while n != 0:
    r = n % 10
    if r == d:
        cont = cont + 1 
    n = n // 10
    
#print(d, "ocorre", cont, "vezes em", num)
print(cont)

