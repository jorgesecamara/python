#Escreva uma função que recebe uma matriz m-por-n de inteiros não negativos e conta o número de linhas e colunas cujos elementos são todos zeros.
#
 #   Exemplo:
#Matriz: 4 x 5
#0 0 0 0 1
#0 0 0 0 0
#0 1 0 0 0
#0 0 0 0 0
#Linhas nulas = 2
#Colunas nulas = 3
#Importante: Seu código deve exibir a mensagem similar ao formato acima, para que seja corrigido corretamente (em particular, você deve ter a mensagem Linhas nulas = numero e Colunas nulas = numero nessa ordem, e nenhuma outra mensagem deve ter o sinal de igualdade.) 

def leiamatriz():
    ''' 
      Função que lê do teclado o número nlinhas de linhas
      e o número ncolunas de colunas e os elementos de
      uma matriz de dimensão nlinhas x ncolunas.

      A função cria e retorna a matriz lida.
    '''
    nlinhas  = int(input("Número de linhas: "))
    ncolunas = int(input("Número de colunas: "))
    matriz = []
    # TERMINAR
    for i in range(nlinhas):
        linha = []
        for j in range(ncolunas):
            elemento = int(input(f'valor[{i+1}][{j+1}]: '))
            linha.append(elemento)
        matriz.append(linha)
    #
    # ...
    #
    return matriz
    
def exibematriz(matriz):
    '''
    Recebe e imprime uma matriz de inteiros.
    '''
    nlinhas  = len(matriz)
    ncolunas = len(matriz[0])
    # TERMINAR
    for i in range(nlinhas):
        for j in range(ncolunas):
            print(f'{matriz[i][j]}', end=' ')
        print()
    #
    # ...
    
def contazeros(matriz):
    ''' Conta número de linhas e colunas contendo apenas zeros 
    
    Deve exibir mensagem
    
    Linhas nulas = x
    Colunas nulas = y
    
    onde x e y são os número de linhas e colunas nulas, respectivamente.
    ''' 
    # FAZER
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    x = 0
    y = 0
    T = []
    for i in range(ncolunas):
        linha = []
        for j in range(nlinhas):
            elemento = 0
            linha.append(elemento)
        T.append(linha)
    for i in range(nlinhas):
        for j in range(ncolunas):
            T[j][i] = matriz[i][j]
    nlinhast = len(T)
    
    for i in range(nlinhas):
        n = 0
        if matriz[i].count(0) == len(matriz[0]):
            x += 1
    for n in range(nlinhast):
        if T[n].count(0) == len((T[0])):
            y +=1
    print(f'Linhas nulas = {x}')
    print(f'Colunas nulas = {y}')
        #

def main():
    '''
    Programa que lê n e uma matriz de inteiros n x n
    e verifica se a matriz e simétrica.
    '''
    A = leiamatriz ()
    exibematriz (A)
    contazeros (A)

# NAO MODIFICAR TRECHO ABAIXO
if __name__ == '__main__':
    main()