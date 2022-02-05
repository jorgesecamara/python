#Dado um número inteiro \( n>0 \)

#, calcular e exibir a soma de todos os inteiros positivos pares estritamente menores que n.

#Exemplo: 
#
 #   Para n=18, exibir 72
  #  Pra n=9, exibir 20

n = int( input("Digite um numero:") )
# Calcular a soma de todos os inteiros pares < n

soma = 0 
for number in range(1, n):
    if (number % 2 == 0):
        #print(number)
        soma = soma + number 
print(soma)

#soma = 0
##calculo da soma
#i=2
#while i <= n:
#    soma = soma + i 
#    i = i + 2
#print(soma)

#soma = 0
#
#i = 2 
#while i <= n:
#    soma = soma + i
#    i = i +1 
#print("A soma dos ", n, "primeiros inteiros positivos é", soma)