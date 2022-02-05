#Escreva um programa estruturado que recebe do usuário um inteiro n > 0 e uma lista de n números inteiros e os exibe na ordem inversa de entrada. Seu programa deve ter uma função inverso que recebe uma lista e exibe (print) os números em ordem inversa, uma  função  main que lê a sequência de números entrados pelo usuário, os salva em uma lista e chama a função inverso para mostrar o resultado.
#Exemplo: 
#Para n = 3 e a sequência de entrada 3 42 105 o programa deve exibir 105 42 3

def inverso(lista: list) -> list:
    " Devolve lista contendo elementos de 'lista' em ordem inversa. "
    # fazer
    n = lista[::-1]
    return n
    ou
    s = len(lista)
    for c in (s-1,-1,-1):
        print(lista[c])

    

def main():
    '''
    Funcao principal do programa
    
    Le um numero n > 0 e uma sequencia de n inteiros e os exibe em ordem inversa
    usando a funcao 'inverso'. 
    '''
    # fazer
    n = int(input('n: '))
    numero = []
    resp = []
    while n > 0:
        numero.append(int(input("Numero: ")))
        n = n - 1
    return inverso(numero)
    

# NAO ALTERE O TRECHO ABAIXO
if __name__ == '__main__':
    main()