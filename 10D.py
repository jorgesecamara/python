#Faça um programa estruturado que lê um número inteiro n > 0 e para cada número entre 1 e n indica se ele pode ser escrito como a soma de dois primos positivos (não necessariamente distintos). Por exemplo, 4 pode ser escrito como 2+2 e 5 como 2+3.  Note que qualquer inteiro pode ser escrito como x = (x-i) + i, para 1 < i < x, e o resultado é verdade se e somente se (x-i) e i forem primos.
#Exemplo:
#    Para n = 6 o programa deve exibir
#    1 não é soma de primos
#    2 não é soma de primos
#    3 não é soma de primos
#    4 é soma de primos
#    5 é soma de primos
#Seu programa deve ter uma função primo que determina se um inteiro é primo e uma função eh_soma que determina se um inteiro é a soma de dois primos. Seu programa também deve ter uma função main, que lê um inteiro digitado pelo usuário, chama a função eh_soma e exibe as respostas, além  do trecho de código padrão que chama a função main ao final.

def primo(n: int) -> bool:
    " Devolve True se n e' primo e False caso contrario. "
    # fazer
    tot = 0
    for c in range(1, n+1):
        if n % c == 0:
            tot += 1
    if tot == 2:
        return True
    else:
        return False
        
def eh_soma(n: int) -> bool:
    " Devolve True se n e' a soma de dois primos e False caso contrario. "
    # fazer
    t = 0
    for i in range(1, n + 1):
        a = primo(i)
        b = primo(n-i)
        if b == True and a == True and (n - i) + i == n:
            t += 1
    if t > 0:
        return True
    else:
        return False 


   
def main():
    '''
    Funcao principal do programa
    
    Le um numero n digitado pelo usuario, e para cada numero 1 < x < n determina
    se x e' a soma de dois primos e caso seja, exibe os somandos. 
    '''
    # fazer
    num = int(input('Digite um numero: '))
    for c in range(1, num):
        if eh_soma(c) is True:
            print(f' {c} é a soma de dois primos')
        else:
            print(f' {c} Não é a soma de DOis primos')
    

# NAO ALTERE O TRECHO ABAIXO
if __name__ == '__main__':
    main()