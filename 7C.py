#Um inteiro 99<n<100 é um número de Armstrong se ele é igual a soma dos cubos de seus dígitos. Por exemplo, 153 é um número de Armstrong pois 153=13+53+33
#Escreva um programa que lista todos os números de Armstrong em ordem crescente. Seu programa deve exibir cada número em uma linha distinta.

# Encontrar numeros de Armstrong entre 100 e 999 (inclusos)
num = []
list = []
for c in range(100, 1000):
    num.append(c)
for i in num:
    cen = (i // 100 % 10)
    dez = (i // 10 % 10)
    uni = (i // 1 % 10)
    if cen ** 3 + dez**3 + uni **3 == i:
        list.append(i)
list.sort()
for l in list:
    print(l)
