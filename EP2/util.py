import copy

colors = {
   -1: ';'.join([str(7), str(30), str(40)]),
    0: ';'.join([str(1), str(30), str(40)]),
    1: ';'.join([str(1), str(31), str(41)]),
    2: ';'.join([str(1), str(32), str(42)]),
    3: ';'.join([str(1), str(33), str(43)]),
    4: ';'.join([str(1), str(34), str(44)]),
    5: ';'.join([str(1), str(35), str(45)]),
    6: ';'.join([str(1), str(36), str(46)])
}

def exibe_tabuleiro(matrix:list) -> None:
    nrow = len(matrix)
    ncol = len(matrix[0])
    print(end='\x1b[7;30;47m\x1b[1;30;40m   ')
    for j in range(ncol):
        print(f' {matrix[0][j]} ', end = '')
    print()
    for i in range(1,nrow-1):
        print(end=f'\x1b[7;30;47m{i:3}')
        for j in range(ncol):
            print(f'\x1b[{colors[matrix[i][j]]}m {matrix[i][j]} ', end = '')
        print()
    print(end='\x1b[1;30;40m   ')
    for j in range(ncol):
        print(f' {matrix[-1][j]} ', end = '')
    print()
    print(end='\x1b[7;30;47m      ')
    for i in range(ncol-2):
        print(f' {chr(65+i)} ', end = '')
    print('   \x1b[0m')


def exibe_tabuleiro_sem_cores(matrix:list) -> None:
    nrow = len(matrix)
    ncol = len(matrix[0])
    print('   ╭─', '──'*(ncol-2), '╮', sep='')
    for i in range(1,nrow-1):
        print(f'{i:2} │', end = ' ')
        for j in range(1,ncol-1):
            print(matrix[i][j], end = ' ')
        print('│')
    print('   ╰─', '──'*(ncol-2), '╯', sep='')
    print(end='     ')
    for i in range(1,ncol-1):
        print(chr(64+i), end = ' ')
    print()

def exibe_tabuleiro_sem_cores_ascii(matrix:list) -> None:
    nrow = len(matrix)
    ncol = len(matrix[0])
    for i in range(1,nrow-1):
        print(f'{i:2} |', end = ' ')
        for j in range(1,ncol-1):
            print(matrix[i][j], end = ' ')
        print()
    print(end='     ')
    for i in range(1,ncol-1):
        print(chr(64+i), end = ' ')
    print()

def contrai_aresta(G:dict, i:int, j:int) -> None:
    " Contrai aresta i e j de grafo representado por dicionário de adjacência G. "
    # remova aresta i -- j
    G[j].remove(i)
    G[i].remove(j)
    # conecte i aos vizinhos de j
    G[i].update(G[j])
    for v in G[j]: # remova arestas incidentes a j e conecte
        G[v].remove(j)
        G[v].add(i)
    # remova j
    del G[j]

def gera_grafo(T:list) -> (dict, dict):
    " Devolve grafo das regiões de tabuleiro T. "
    nlin, ncol = len(T), len(T[0]) # tamanho do tabuleiro
    # Vamos inicialmente criar um grafo contendo um nó para cada posição do tabuleiro
    # conectado a sua 4-vizinhança
    G, C = {}, {} # grafo, coloração
    # vamos numerar vértices da esquerda p/ direita, de cima p/ baixo
    offset = ncol-2 # diferença entre vértices de linhas adjacentes
    # quina esquerda superior: i=1,j=1
    G[0] = {1, offset}
    C[0] = T[1][1]
    # quina direita superior
    k = ncol-3 # i=1, j=ncol-2
    G[k] = {k-1, k+offset}
    C[k] = T[1][ncol-2]
    # quina esquerda inferior: i=nlin-2,j=1
    k = (nlin-3)*offset
    G[k] = {k-offset, k+1}
    C[k] = T[nlin-2][1]
    # quina direita inferior: i=nlin-2,j=ncol-2
    k = (nlin-3)*offset + (ncol-3)
    G[k] = {k-offset, k-1}
    C[k] = T[nlin-2][ncol-2]
    # borda superior: i=1
    for j in range(2,ncol-2):
        k = j-1
        G[k] = {k-1, k+1, k+offset}
        C[k] = T[1][j]
    # borda esquerda: j=1
    for i in range(2,nlin-2):
        k = (i-1)*offset
        G[k] = {k-offset, k+1, k+offset}
        C[k] = T[i][1]
    # borda direita: j=ncol-2
    for i in range(2,nlin-2):
        k = (i-1)*offset + (ncol-3)
        G[k] = {k-offset, k-1, k+offset}
        C[k] = T[i][ncol-2]
    # borda inferior: i=nlin-2
    for j in range(2,ncol-2):
        k = (nlin-3)*offset + (j-1)
        G[k] = {k-offset,k-1,k+1}
        C[k] = T[nlin-2][j]
    # região interna
    for i in range(2,nlin-2):
        for j in range(2,ncol-2):
            # linearização para obter nome do vértice
            k = (i-1)*offset + (j-1)
            # acima, esquerda, direita, abaixo
            G[k] = {k-offset, k-1, k+1, k+offset}
            C[k] = T[i][j]
    # Agora reduzimos o grafo enquanto possível, unindo nós vizinhos de mesma cor
    # até que grafo seja independente maximal
    colapsou = True
    while colapsou:
        colapsou = False
        # encontra aresta com duas pontas de mesma cor
        for u in G:
            for v in G[u]:
                if C[u] == C[v]:
                    colapsou = True
                    break
            if colapsou:
                break
        if colapsou: # colapsa aresta
            contrai_aresta(G, u, v)
            del C[v] # não precisamos mais da cor
    return G, C

def pinta_vertice(G:dict, C:dict, n:int, c:int):
    " Pinta nó n com cor c e atualiza grafo G e coloração C. "
    if n not in G:
        return
    Gp = copy.deepcopy(G)
    Cp = copy.deepcopy(C)
    # altere cor de nó n
    Cp[n] = c
    # agora percorra vizinhos de n
    for v in G[n]:
        if C[v] == c: # se vizinho é da mesma cor, colapse aresta
            contrai_aresta(Gp,n,v)
            del Cp[v]
    return Gp, Cp