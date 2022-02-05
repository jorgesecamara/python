'''Uma matriz quadrada A é simétrica se A[i][j] == A[j][i] para toda linha i e coluna j.

Escreva um programa estruturado que uma matriz quadrada de tamanho n-por-n do usuário e determina se ela é simétrica.

Exemplos:
A matriz

[[1,2,3],
 [2,1,4],
 [3,4,1]]

é simétrica. 


A matriz

[[1,2,3],
 [2,1,4],
 [1,2,3]]

não é simétrica'''

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
    for i in range(nlinhas):
        linha = []
        for j in range(ncolunas):
            elemento = int(input('valor: '))
            linha.append(elemento)
        matriz.append(linha)
    # TERMINAR
    #
    # ...
    #
    return(matriz)
    
def exibematriz(matriz):
    '''
    Recebe e imprime uma matriz de inteiros.
    '''
    nlinhas  = len(matriz)
    ncolunas = len(matriz[0])
    # TERMINAR
    for i in range(nlinhas):
        for j in range(ncolunas):
            print(f'[{matriz[i][j]}]', end='')
        print()
    #
    # ...
    
def simetrica(matriz) -> bool:
    '''
    Recebe uma matriz e retorna True se a matriz for simétrica,
    em caso contrário retorna False.

    Pre-condição: a função supõe que a matriz é quadrada
    '''
    # FAZER
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    T = []
    for i in range(nlinhas):
        linha = []
        for j in range(ncolunas):
            elemento = 0
            linha.append(elemento)
        T.append(linha)
    
    for i in range(nlinhas):
        for j in range(ncolunas):
            T[j][i] = matriz[i][j]
        nlinhast = len(T)
        ncolunasT = len(T[0])
    if nlinhas == nlinhast and ncolunas ==ncolunasT:
        for n in range(nlinhas):
            for c in range(ncolunas):
                if matriz[n][c] != T[n][c]:
                    return False
        else: return True
    else:
        return False
    #

def main():
    '''
    Programa que lê n e uma matriz de inteiros n x n
    e verifica se a matriz e simétrica.
    '''
    A = leiamatriz ()
    exibematriz (A)
    if simetrica (A):
        print("Matriz é simétrica.")
    else:
        print("Matriz não é simétrica.")

# NAO MODIFICAR TRECHO ABAIXO
if __name__ == '__main__':
    main()