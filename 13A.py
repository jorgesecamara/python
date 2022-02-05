#Implemente uma função crie_matriz, que recebe inteiros m e n e um real x, cria e devolve uma matriz de tamanho m-por-ncujos elementos são todos iguais ax.
#Exemplo:
#    Para m = 4, n = 5 e x = 10
#    Retorno: 
 #   [[10.0, 10.0, 10.0, 10.0, 10.0], 
 #    [10.0, 10.0, 10.0, 10.0, 10.0], 
 #    [10.0, 10.0, 10.0, 10.0, 10.0], 
 #    [10.0, 10.0, 10.0, 10.0, 10.0]]

def criematriz(m:int, n:int, valor:float):
    ''' 
    Cria e retorna uma matriz com m linhas e n colunas
    em que cada elemento é igual ao valor dado.
    '''    
    matriz = [] # lista vazia
    # COMPLETAR:
    for i in range(m):
        linha = []
        for j in range(n):
            elemento = valor
            linha.append(elemento)
        matriz.append(linha)
    # CRIAR MATRIZ
    # 
    return matriz


def main():
    '''
        Testa criacao de matriz 4-por-5
    '''
    A = criematriz(4,5,10.0)
    A[1][2] = 2.0 # apenas o elemento da linha 1 coluna 2 deve ser alterado
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end = ' ')
        print()

# NAO MODIFICAR TRECHO ABAIXO
if __name__ == '__main__':
    main()

