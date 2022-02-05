#Dados um número inteiro n>0 e uma sequência com n números reais, determinar
#a maior soma de um segmento da sequência. Um segmento é uma subsequência de números consecutivos. Escreva seu programa de forma estruturada contendo funções soma, fatia e main.#
#
#Exemplo:#
#
 #   n = 12
  #  sequência = [5, -2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1]
   # Saída:
    #    A soma do segmento de soma máxima é 3+14+10-3+9 = 33

def soma(lista: list) -> float:
    ''' 
    Recebe em `lista` uma lista de floats e devolve a
    soma dos seus elementos.
    '''
    # fazer
    v = float(sum(lista))
    return float(v)
    

def fatia(lista:list, ini:int, fim:int) -> list:
    ''' 
    Recebe uma lista lista e inidice ini e fim e
    devolve a sublista (= fatia) formada pelos elementos de
    índices ini, ini+1, ..., fim-1.
    '''
    # fazer
    fatiada = []
    for c in lista[ini: fim]:
        fatiada.append(c)
    return list(fatiada)


def main():
    #'''
    #   Programa que lê n > 0 e uma sequência com n
    #   números reais e calcula a maior soma de
    #   um de seus segmentos.
    #'''
    n = int(input("Digite n:"))
    # leia a sequência
    lista = []
    for i in range(n):
        num = float(input("Digite um número: "))
        lista.append(num)
    # TERMINAR
    maior = lista[0]
    for i in range(n):
        for j in range(i + 1, n + 1):
            s = soma(fatia(lista, i, j))
            if s > maior:
                maior = s
                lista2.append(fatia(lista, i, j))
    
    print('-'*30)
    print(lista2[-1])
    print(maior)



# NAO MODIFICAR TRECHO ABAIXO
if __name__ == '__main__':
    main()
