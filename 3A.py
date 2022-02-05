#Dados inteiros a e b pelo usuário, computar a soma de todos os inteiros x tal que a<=x<b
a = int( input("Digite a: "))
b = int( input("Digite b: "))

soma = 0 # valor inicial
ini = a
fim = b

while ini < fim:
    soma = soma + ini 
    ini = ini + 1
    
# resultado
print(soma)

# a <= x < b