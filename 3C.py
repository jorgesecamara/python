#Dado um número inteiro positivo exibir o número obtido invertendo as ordem de seus dígitos (ou seja, lendo-o de trás para frente). Se o número for múltiplo de 10, a saída não precisa mostrar os dígitos insignificantes (ou seja, os 0s à esquerda).
#Exemplos:
#Entrada: 12345
#Saída:   54321

#Entrada: 120
#Saída: 21

n = int(input("Digite n: "))

s = 0
while n > 0:
    d = n % 10
    n = n // 10
    s = s*10 +d
    
print( s)