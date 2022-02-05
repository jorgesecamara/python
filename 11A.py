#Dados um inteiro n > 0 e n lançamentos de uma roleta (números entre 0 e 36), calcular a frequência de ocorrência de cada número. Exiba apenas os lançamentos com alguma ocorrência (ou seja, frequência positiva).
#Exemplo:
#Digite n: 5
#Lancamento: 1
#Lancamento: 1
#Lancamento: 30
#Lancamento: 12
#Lancamento: 2
#Numero 1 ocorreu 2 vezes
#Numero 1 ocorreu 2 vezes
#Numero 2 ocorreu 1 vez
#Numero 12 ocorreu 1 vez
#Numero 30 ocorreu 1 vez
#Importante: o corretor verifica apenas os números, na ordem em que são exibidos

def main():
    # Escreva seu programa aqui
    n = int(input('numero de lançamento: '))
    numero = []
    resp = []
    while n > 0:
        numero.append(int(input("Numero: ")))
        n = n - 1
    for c in range(0, 37): 
        if c in numero:
            print(c, numero.count(c))
            #print(f' numero {c} ocorreu [numero.count(c)} vezes')
            resp.append(c)
    return resp

    
    
# NAO ALTERE O TRECHO ABAIXO
if __name__ == "__main__":
    main()