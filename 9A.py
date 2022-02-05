#Dados um inteiro n >= 0 computar e exibir n!
#Exemplos:
#    3! = 6
#    5! = 120 
#    10! = 3 628 800

def fatorial(c = int):
    f= 1
    while c > 0:
        f *= c
        c -= 1
        
    return int(f)
n = int(input('digite um numero: '))
print(fatorial(n))


# def fatorial(n = int) -> int:
#     " Recebe um inteiro n >= 0 e devolve n! "

#     #inicializador
#     i = 1
#     n_fat = 1 
    
#     #calculo do n!
#     while i <= n:
#         n_fat = n_fat * i
#         i = i + 1
        
#     return(int(n))
#     #return(n_fat)
    
# n = int(input("Digite um número inteiro não-negativo: "))
# a = fatorial(n)
# print(a)
    


