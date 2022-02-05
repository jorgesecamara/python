#Escreva um programa que recebe do usuário os valores dos coeficientes de um polinômio de segundo grau e exibe as suas raízes reais em ordem crescente, se elas existirem, caso contrário exibe o número 0.
#Por exemplo, dado
#a = 1
#b = -3
#c = 2
#representando o polinômio
#1⋅x2−3⋅x+2
#exibir
#1.0 2.0
#Dado 
#a = 1
#b = -1
#c = 4
#exibir
#0
#Lembre-se: um polinômio do segundo grau possui raízes reais se e apenas se o determinante 
#b2−4∗a∗c
#for não-negativo.
#Nota: use a função sqrt para calcular a raiz quadrada de um número

from math import sqrt # precisamos disso para usar a funcao sqrt

a = int(input('digite valor para "a": '))   # receber valor do coeficiente a
b = int(input('digite valor para "b": '))
c = int(input('digite valor para "c": '))
delta = b**2 - 4*a*c
if delta >= 0:
    x1 = ((b*-1) - sqrt(delta))/(2 * a)
    x2 = ((b*-1) + sqrt(delta))/(2 * a)
    print(x1,x2)
else:
    x1 = 0
    x2 = 0
    print('0')

# # Usar formula de Baskhara: x = (-b  +- sqrt(b**2 - 4*a*c))/2
# x1 = sqrt(2)    
# x2 = sqrt(9)   
# print( x1, x2 )  # exibir as raizes do polinomio com x1 < x2