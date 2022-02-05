#Escreva um programa estruturado que recebe uma lista de números reais e exibe apenas os números acima da média (um número por linha).
#Exemplo: 
#Para a sequência 3,7,8 o programa deve exibir os número 7,8
#Seu programa deve ter uma função media que recebe uma lista e devolve a média dos seus itens, uma função acimade que recebe uma lista e um número real e retorna uma lista contendo apenas os elementos da lista estritamente maiores que o número dado, e uma função  main que lê uma sequência de números entrados pelo usuário, os armazena em uma lista e chama as outras funções para mostrar o resultado desejado.

def media(lista: list) -> float:
    " Devolve a media dos elementos de 'lista'. "
    # fazer
    media = sum(lista)/len(lista)
    return media
    
def acimade(lista: list, limiar: float) -> list:
    " Devolve lista com os elementos de 'lista' > 'limiar'. "
    # fazer
    resp = []
    for c in lista:
       if c > limiar:
           resp.append(c)
    return resp


def main():
    '''
    Funcao principal do programa
    
    Le um numero n > 0 e uma sequencia de n reais e exibe os numeros acima da 
    media. 
    '''
    # fazer
    n = int(input("numero de n: "))
    numero = []
    resp = []
    while n > 0:
        numero.append(int(input("Numero: ")))
        n = n - 1
        

    return acimade(numero, media(numero))
    

# NAO ALTERE O TRECHO ABAIXO
if __name__ == '__main__':
    print(main())