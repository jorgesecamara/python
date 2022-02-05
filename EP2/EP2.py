### Segundo projeto ###########################################################
# Use este arquivo como base para sua solucao
# Modifique apenas os trechos indicados
###############################################################################

### NAO MODIFICAR A PARTE ABAIXO ##############################################
import string
from util import exibe_tabuleiro, gera_grafo, pinta_vertice, exibe_tabuleiro_sem_cores
### NAO MODIFICAR A PARTE ACIMA ###############################################

### MODIFICAR A PARTIR DAQUI ##################################################
def carrega_tabuleiro(nome: str) -> (int, int, list):
    """
    Dado um nome de arquivo contendo a descricao de um problema, le e devolve:
        - inteiro representando a dificuldade (int 1-3)
        - numero maximo de acoes (int)
        - numero de cores disponiveis (int)
        - matriz de inteiros do tabuleiro contendo moldura

    Argumentos
    ----------
        nome: str
            Nome do arquivo a ser lido.

    Retorna
    -------
        int:
            Dificuldade do quebra-cabeca.
        int:
            Numero de acoes permitidas.
        int:
            Numero de cores disponiveis.
        matriz de inteiros representada como lista de listas:
            Matriz representando o tabuleiro com moldura.
    """
    with open(nome) as arquivo:         
        linhas = arquivo.readlines()
        cabecalho = linhas[0].split(" ")
        dificuldade = int(cabecalho[0])
        qtd_acoes = int(cabecalho[1])
        qtd_linhas = int(cabecalho[2])
        qtd_colunas = int(cabecalho[3])
        qtd_cores = int(cabecalho[4])
        matriz = []
        borda = []
        
        for _idx_coluna in range(qtd_colunas + 2):
            borda.append(0)
        
        matriz.append(borda)
        
        for numeroLinha in range(0, qtd_linhas):
            linha_matriz = [0]
            linha = linhas[numeroLinha + 1].split(" ")
            
            for numeroColuna in range(0, qtd_colunas):
                linha_matriz.append(int(linha[numeroColuna]))
        
            linha_matriz.append(0)
            matriz.append(linha_matriz)
            
        matriz.append(borda)
        
        return dificuldade, qtd_acoes, qtd_cores, matriz
    #return(0,0,0,[[0]])
    
def pinta(tabuleiro: list, lin: int, col: int, cor: int) -> None:
    """
    Pinta a regiao da celula em `lin`, `col` com a `cor` dada.

    Argumentos
    ----------
        tabuleiro: matriz de inteiros representada como lista de listas
            O tabuleiro como uma matriz representada por uma lista de listas.
        lin: int
            A linha da celula inicial cuja regiao deve ser pintada.
        col: int
            A coluna da celula inicial cuja regiao deve ser pintada.
        cor: int
            Cor a ser usada para pintar a regiao.
    """
    cor_original = tabuleiro[lin][col]
    
    if cor_original == cor:
        return
    
    QUEIMANDO = -1
    tabuleiro[lin][col] = QUEIMANDO
    rodar = True
    
    while (rodar):
        rodar = False
        
        for linha in range(len(tabuleiro)):                         
            for coluna in range(len(tabuleiro[linha])):
                if tabuleiro[linha][coluna] == QUEIMANDO:
                    tabuleiro [linha][coluna] = cor 
                    #Acima
                    if tabuleiro[linha + 1][coluna] == cor_original:
                        tabuleiro[linha + 1][coluna] = QUEIMANDO
                    #Abaixo
                    if tabuleiro[linha - 1][coluna] == cor_original:
                        tabuleiro[linha - 1][coluna] = QUEIMANDO
                    #Esquerda
                    if tabuleiro[linha][coluna + 1] == cor_original:
                        tabuleiro[linha][coluna + 1] = QUEIMANDO
                    #Direita
                    if tabuleiro[linha][coluna - 1] == cor_original:
                        tabuleiro[linha][coluna - 1] = QUEIMANDO
                        
        for linha in tabuleiro:
            for coluna in linha:
                if coluna == QUEIMANDO:
                    rodar = True
    return

def verifica_fim(tabuleiro: list) -> bool:
    """
    Dada uma matriz de tabuleiro com moldura, a funcao retorna `True` se o 
    tabuleiro esta monocromatico ou `False` caso contrario.

    Argumentos
    ----------
        tabuleiro: matriz de inteiros representada como lista de listas
            O tabuleiro a ser verificado como uma matriz representada por uma 
            lista de listas.

    Retorna
    -------
        bool
            True se o tabuleiro esta monocromatico, False caso contrario.
    """
    cor_base = tabuleiro[1][1]
    monocromatico = True
    
    for linha in range(1, len(tabuleiro) - 1):
        for coluna in range(1, len(tabuleiro[linha]) - 1):
            if tabuleiro[linha][coluna] != cor_base:
                monocromatico = False
                break
            
        if monocromatico == False:         
            break
    
    return monocromatico
    
def busca(L: dict, C: dict, n_acoes: int) -> (int, int):
    """
    Faz uma busca a procura de uma resolucao do tabuleiro usando o grafo dado 
    pelo dicionario de adjacencia `L`, cores `C`, e numero de acoes restantes. 
    Deve devolver a primeira acao a ser feita (vertice e cor) de uma sequencia
    que faca o grafo posssuir um unico vertice, ou -1, -1, se nao houver
    tal sequencia.

    Argumentos
    ----------
        L: dict
            O dicionario de adjacencia do grafo de regioes coloridas. As chaves 
            de `L` representam os no's do grafo, e o i-esimo elemento representa 
            os vizinhos do vertice `i`, onde `L[i]` e' um set onde os elementos 
            representam os vertices vizinhos de `i`. Por exemplo, o grafo:

                        0
                        |
                G  =    1 - 2
                        |
                        3

            e' representado por:

                L  = {0: {1}, 1: {0, 2, 3}, 2: {1}, 3: {1}}

            As chaves `i` de `L` representam posicoes `y`, `x` como:

                i = (x-1)*(N-2) + (y-1).

            Por exemplo, para um tabuleiro com `M=7` e `N=7`, um nó 
            representando a posição (3,2) será codificado com a chave

                i = (3-1)*(7-2) + (2-1) = 11.

            Desta maneira podemos obter diretamente a posição linha, coluna 
            associada a um nó pela sua chave.

        C: dict
            O dicionario mapeando cada vertice de `L` para uma cor.

        n_acoes: int
            O numero de acoes restantes para completar o jogo.

        Retorna
        -------
            int
                O vertice a ser colorido. Caso seja impossivel resolver o
                quebra-cabeca, retorna -1.
            int
                A cor pintar o vertice. Caso seja impossivel resolver o
                quebra-cabeca, retorna -1.
    """
    if n_acoes < 0:
        return -1, -1
    elif len(L) == 1:
        return None, None
    else:
        for n in L:
            for c in C:
                if c != n:
                    L1, C1 = pinta_vertice(L, C, n, C[c])
                    if busca(L1, C1, n_acoes -1) != (-1, -1):
                        return n, C[c]
    return(-1,-1)

def letra_numero(letras: str) -> int:    #para ela tive q usar o pacote importado foi uma estrategia que encontrei para desenvolver
    colunaNumerica = 0
    for c in letras:
        if c in string.ascii_letters:
            colunaNumerica = colunaNumerica * 26 + (ord(c.upper()) - ord('A')) + 1
    return colunaNumerica

def numero_letra(numero: int) -> str:  
    texto = ""
    while numero > 0:
        numero, resto = divmod(numero - 1, 26)    
        texto = chr(65 + resto) + texto
    return texto

def main() -> int:
    """
    Inicia o jogo pedindo pelo nome do arquivo a ser carregado. Em seguida, 
    executa o jogo, a cada turno recebendo uma posicao e cor ou 'dica'. 
    Se o numero de acoes zerar antes do tabuleiro ser monocromatico ou se
    funcao dica indicar inexistencia de solucao perdido, o programa termina
    exibindo derrota. Caso a jogadora consiga colorir o tabuleiro 
    monocromaticamente dentro do numero de acoes pedido, o programa termina 
    com uma mensagem de parabenizacao.

    A funcao deve devolver um inteiro indicando o resultado da partida.

    Retorna
    -------
        int
            Um inteiro -1 se pediu dica mas o jogo ja esta perdido, 0 se nao 
            conseguiu ganhar no numero de acoes maxima, e 1 se ganhou o jogo.
    """
    print("Bem-vindo ao jogo Papel!")
    nome_arquivo = input("Digite o nome do tabuleiro: ")
    dificuldade, qtd_acoes, qtd_cores, matriz = carrega_tabuleiro(nome_arquivo)
    
    print("Dificuldade:", dificuldade)
    print("Cores:", qtd_cores)
    print("Número máximo de jogadas:", qtd_acoes)
    
    fim_jogo = False
    
    while not fim_jogo and qtd_acoes > 0:
        exibe_tabuleiro_sem_cores(matriz)
        entrada_jogador = input("Digite '<coluna><linha> <cor>' ou 'dica':")
        
        if entrada_jogador == "dica":
            jogada_dica = dica(matriz,qtd_acoes)
            if jogada_dica == (0, 0, 0):
                print("Não há ações válidas")
                qtd_acoes = -1
            else:
                coluna = jogada_dica[1]
                linha = jogada_dica[0]
                cor = jogada_dica[2]
                print("Dica:", str(numero_letra(coluna)) + str(linha), str(cor))
                qtd_acoes -= 1
                pinta(matriz, linha, coluna, cor)
        else:
            entrada_jogador_lista = entrada_jogador.split(" ")
            coluna = letra_numero(entrada_jogador_lista[0][0])
            linha = int(entrada_jogador_lista[0][1])
            cor = int(entrada_jogador_lista[1])
            pinta(matriz, linha, coluna, cor)
            qtd_acoes -= 1
        
        fim_jogo = verifica_fim(matriz)
    
    exibe_tabuleiro_sem_cores(matriz)
   
    if verifica_fim(matriz):
        print("Parabéns!")
        return 1  
    else:
        print("O problema não foi resolvido")
        if qtd_acoes == 0:
            return 0
        else:
            return -1
                 
    
    #Renato, tentei debuggar essa parte, mas não consegui melhorar, quando eu altero ele comenta mesma coisa só q invertido o 1 e 0. 
    #Não conseugi localizar o que eu poderia fazer lá em cima para melhorar, espero que pelo menos esteja satisfatório
    
    
    # if verifica_fim(matriz):
    #     print("Parabéns!")
    #     return 1
    #     else:
    #         print("O problema não foi resolvido")
    #         if qtd_acoes == 0:
    #             return 0
    #         else: 
    #             return -1 
    
    # if verifica_fim(matriz):
    #     print("Parabéns!")
    #     return 0  #1#0
    # else:
    #         print("O problema não foi resolvido")
    #         return 1  #0#1
        
    
# NAO MODIFIQUE AS LINHAS ABAIXO ##############################################
def dica(T: list, acoes: int) -> tuple:
    """
    Da uma dica para resolver o tabuleiro T em um numero de coloracoes menor ou 
    igual a acoes.

    Recebe a matriz do problema e o numero de acoes restantes e devolve uma 
    jogada (localizacao `lin`, `col` e uma `cor`). Se o problema tiver solucao, 
    a jogada deve ser otima, no sentido que leva o jogo a uma configuracao da 
    qual se pode resolver o problema. Se o problema nao tiver solucao devolve 
    (0,0,0).

    Argumentos
    ----------
        T: matriz de inteiros representada como lista de listas
            O tabuleiro do jogo atual.
        acoes: int
            O numero de acoes restantes.

    Retorna
    -------
        int:
            A linha a ser colorida pela acao dada pela dica. Retorna 0 caso o 
            jogo ja esteja perdido.
        int:
            A coluna a ser colorida pela acao dada pela dica. Retorna 0 caso o 
            jogo ja esteja perdido.
        int
            A cor a ser usada pela acao dada pela dica. Retorna 0 caso o jogo 
            ja esteja perdido.
    """
    nlin, ncol = len(T), len(T[0]) # dimensoes da matriz do tabuleiro
    L, C = gera_grafo(T) # gera um grafo das regioes do tabuleiro T
    n, c = busca(L, C, acoes) # devolve vertice e cor de acao pintar
    if n == -1 or c == -1: # se busca nao encontrou solucao
        return(0, 0, 0)
    # caso contrario decodifica posicao a partir do vertice devolvido
    i, j = n // (ncol-2) + 1, n % (ncol-2) + 1
    return(i, j, c)
    
if __name__ == '__main__':
    main()