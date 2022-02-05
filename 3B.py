#Dados um inteiro n > 1 e uma sequência com n números inteiros, verificar se a sequência é uma progressão aritmética (PA). Exibir True se sequência for PA e False caso contrário.

#Uma sequência x1,...,xn é uma PA se existe r tal que xk − xk−1 = r para todo k = 2,...,n.

#Exemplos:

    #A sequência 1, 3, 5, 7, 9 é uma PA.
    #A sequência 1, 4, 5, 7, 9 não é uma PA


n = int(input("Tamanho da sequencia (n > 2): "))
# obter dois primeiros numeros para determinar razao da possivel PA
anterior = int(input("Numero: "))
atual = int(input("Numero: "))

razao = atual - anterior
n = n - 2 # ja' lemos dois numeros

eh_pa = True # sequencia parcial e' PA
while n > 0:
    n = n - 1
    anterior = atual
    # Obter proximo numero da sequencia
    atual = int(input("Numero: "))
    # Verificar se e' pa e atualizar variaval eh_pa
    pa = atual - anterior 
    if pa != razao:
        eh_pa = False 
        
print( eh_pa )
