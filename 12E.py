#Dados um número inteiro n>0 e uma sequência com n números reais, determinar
#a maior soma de um segmento da sequência. Um segmento é uma subsequência de números consecutivos. Escreva seu programa de forma estruturada contendo funções soma e main.#
#
#Exemplo:#
#
 #   n = 12
  #  sequência = [5, -2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1]
   # Saída:
    #    A soma do segmento de soma máxima é 3+14+10-3+9 = 33

def soma(lista:list, ini:int, fim:int) -> float:
 #   ''' 
 #   Recebe em `lista` uma lista de números e índices
  #  `ini` e `fim` da lista e devolve a soma#
#
 #       lista[ini] + lista[ini+1] + ... + lista[fim-1]
#
 #   Pre-condição: a função supõe que
#
 #       0 <= ini < fim <= len(lista)        
   # '''
    # fazer
    return sum(lista[ini: fim])
    

def main():
    '''
       Programa que lê n > 0 e uma sequência com n
       números reais e calcula a maior soma de
       um de seus segmentos.
    '''
    n = int(input("Digite n: "))
    # leia a sequência
    lista = []
    for i in range(n):
        num = float(input("Digite um número: "))
        lista.append(num)
    maior = lista[0]
    for i in range(n):
        for j in range(i+1,n+1):
            s = soma(lista,i,j)
            if s > maior:
                maior = s
    print(maior)

if __name__ == '__main__':
    main()
