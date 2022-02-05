#Escreva um programa estruturado que recebe um número inteiro n > 0 e determina se ele é primo. Seu programa deve ter uma função primo que recebe um inteiro e retorna True se ele é primo e False em caso contrário. Ele também deve seguir o modelo de programa estruturado, com uma função main que trata das entradas e saídas do programa (inputs e prints) e chama a função primo). 
#Atente para caso especial n = 1 não é primo
#Exemplos:
#    5 é primo
#    169 não é primo
#    12 não é primo
#    17 é primo

def primo(n: int) -> bool:
    " Devolve True se n e' primo e False caso contrario. "
    # fazer
    
    tot = 0
    for c in range(1, n + 1):
        if n % c == 0:
            tot += 1 
    if tot == 2:
        return True
    else:
        return False
    
   
def main():
    '''
    Funcao principal do programa
        Le um numero digitado pelo usuario, chama a funcao primo
    para verificar se ele e' primo e exibe o resultado.
    '''
    # fazer
    num = int(input('digite n: '))
    return primo(num)
    

# NAO ALTERE O TRECHO ABAIXO
if __name__ == '__main__':
    main()
