#O Teorema Fundamental da Aritmética diz que qualquer número inteiro maior que 1 pode ser escrito como um produto de número primos. Por exemplo, 6=2*3 e 600=(2**3)*3*(5**2). Os números primos que compõe o produto são chamados fatores e os exponentes de multiplicidades.
#Escreva um programa estruturado que lê um número inteiro n > 1 e descreve sua decomposição em fatores primos e suas multiplicidades.
#Exemplo: Para n = 600 o programa deve exibir
#    fator 2, multiplicidade 3
#    fator 3, multiplicidade 1
#    fator 5, multiplicidade 2
#Seu programa deve ter uma função multiplicidade que determina quantas vezes um inteiro pode ser divido por outro inteiro e uma função main, que lê um inteiro digitado pelo usuário, usa a função multiplicidade para determinar os fatores e as multiplicidades e exibir a saída esperada.
def multiplicidade(n: int, m: int) -> int:
    ''' Computa o numero de vezes que n pode ser dividido por m,
        ou seja, devolve o maior k >= tal que m**k divide n.
        Note que se m não dividir n, k = 0.
    '''
    # fazer
    k = 0
    while n % m == 0:
        k += 1
        n = n/m
    return k 
   
def main():
    '''
    Funcao principal do programa
    
    Le um numero n digitado pelo usuario, e exibe decomposicao em fatores
    primos e suas multiplicidades. 
    '''
    # fazer
    n = int(input('Digite Numero n: '))
    primos = []
    for x in range(2, n+1):
        cont = 0
        for y in range(1, x+1):
            if x % y == 0:
                cont += 1
            if cont <= 2:
                primos.append(x)
    for c in primos:
        if multiplicidade(n, c) > 0:
            print(f'fator {c}, multiplicidade {multiplicidade(n, c)}')
    
# NAO ALTERE O TRECHO ABAIXO
if __name__ == '__main__':
    main()