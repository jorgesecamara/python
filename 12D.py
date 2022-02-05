#Dados n>0 e uma sequência com n
#números reais, escreva um programa que conta e imprime o número de vezes que cada número ocorre na sequência. Escreva seu programa de forma estruturada com funções insira_novo e main.
#Exemplo:
#igite n: 6
#Numero: 1.0
#Numero: 1.0
#Numero: 1.0
#Numero: 3.1
#Numero: 3.1
#Numero: 5.2
#Numero 1.0 ocorreu 3 vezes
#Numero 3.1 ocorreu 2 vezes
#Numero 5.2 ocorreu 1 vez

def insira_novo(x:float, lista:list) -> int:
    '''
    Devolve a posição em que x ocorre em lista.
    Caso x não ocorra em lista, insere x no final (e devolve sua posição).
    '''
    # fazer
    pos = 0
    if x in lista:
        for k, v in enumerate(lista):
            if v == x:
                pos = k
        return pos
    else:
        lista.append(x)
        return lista.index(x)

# NAO ALTERE O TRECHO ABAIXO
def main():
    n = int(input("Digite n: "))
    seq = [] # números vistos
    cont = [] # contagens
    while n > 0:
        n = n - 1
        num = float(input("Numero: "))
        j = insira_novo(num,seq)
        if j >= len(cont):
            cont.append(1)
        else:
            cont[j] += 1
    i = 0
    while i < len(seq):
        sufixo = ""
        if cont[i] > 1:
            sufixo = "es"
        print(f"Numero {seq[i]} ocorre {cont[i]} vez{sufixo}")
        i = i + 1

if __name__ == '__main__':
    main()