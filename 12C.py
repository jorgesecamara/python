#Dados n>0 e uma sequência com n
#números reais, escreva um programa que conta e imprime o número de vezes que cada número ocorre na sequência. Escreva seu programa de forma estruturada com funções posicao e main.
#Exemplo:
#igite n: 6
#Numero: 1.0
#Numero: 1.0
#Numero: 1.0
#Numero: 3.1
#Numero: 3.1
#Numero: 5.2#
#Numero 1.0 ocorreu 3 vezes
#Numero 3.1 ocorreu 2 vezes
#Numero 5.2 ocorreu 1 vez

# Implemente a funcao abaixo para que o programa
# conte as ocorrencias de numeros de uma dada sequencia
def posicao(x:float, lista:list) -> int:
    '''
    Devolve a posição da primeira ocorrência de x em lista.
    Caso x não ocorra em lista, Devolve -1.
    '''
    # fazer
    if x in lista:
        return lista.index(x)
    else:
        return -1
    

# NAO ALTERE O TRECHO ABAIXO
def main():
    n = int(input("Digite n: "))
    seq = [] # números vistos sem repeticao
    cont = [] # no. de ocorrências
    while n > 0:
        n = n - 1
        num = float(input("Numero: "))
        j = posicao(num, seq)
        if j >= 0:
            cont[j] += 1
        else:
            seq.append(num)
            cont.append(1)
    i = 0
    while i < len(seq):
        if cont[i] > 1:
            sufixo = "es"
        else:
            sufixo = ""
        print(f"Numero {seq[i]} ocorreu {cont[i]} vez{sufixo}")   
        i = i + 1

if __name__ == '__main__':
    main()