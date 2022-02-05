#Implemente a função busca, que recebe duas strings r e s e determina o número de vezes que r ocorre em s, sem distinguir minúsculas e maiúsculas.
#Exemplos:
#s = "Um avião é uma casa com asas."
#r = "Asa"
#Devolve: 2
#s = "Um outro exemplo do anterior."
#r = "o "
#Devolve: 3
#Note que a ocorrência se refere a string, e não a palavras.
#Por exemplo:
#s = "Um outro exemplo do anterior."
#r = "o e"
#Devolve: 1

def busca (s:str, r:str):
    ' Devolve o número de ocorrências de r em s. '
    #cont = 0
    s = s.lower()
    cont = s.count(r.lower())
    
    # ...
    # ...
    return cont

def main():
    '''
    Le texto do usuario e exibe palavras
    '''
    texto = input("Digite um texto: ")
    palavra = input("Digite uma palavra para buscar: ")
    co = busca(texto, palavra)
    print(palavra, "ocorre", co, "vezes em", texto)

# NAO MODIFICAR TRECHO ABAIXO
if __name__ == '__main__':
    main()