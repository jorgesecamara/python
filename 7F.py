#O primorial de um inteiro n, escrito n#, é o produto dos números primos menores ou iguais a n. Por exemplo
#11#=2∗3∗5∗7∗11=2310
#e
#12#=2∗3∗5∗7∗11=2310
#Dado um inteiro n > 1, calcular e exibir seu primorial.
#Exemplos:
#    6# = 30.
#    13# = 14# = 15# = 16# = 3030.
#    17# = 510510.

n = int(input("Digite n: "))
primos = []
for x in range(1, n+1):
    cont = 0
    for y in range(1, x+1):
        if x % y == 0:
            cont +=1
    if cont <=2:
        primos.append(x)
# iniciar como elemento neutro da multiplicacao
primorial = 1
for c in primos:
    primorial *= c
# exbir resultado    
print( primorial )