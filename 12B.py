#Dada uma sequência de n > 0 números inteiros, exibir seus elementos eliminando as repetições. Exiba um número por linha
#Faça seu programa de forma estruturada contendo funções pertence e unicos.
#Exemplo:#
#Tamanho: 4
#Numero: 1
#Numero: 2
#Numero: 1#
#Numero: 2
#Sequencia sem repetição: 
#1
#2

def pertence(elem, lista):
    " Devolve True se elem é elemento de 'lista' e False caso contrário. "
    # fazer
    if elem in lista:
        return True
    else:
        return False
    
def unicos(lista):
    " Devolve lista sem elementos duplicados. "
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l 
    
# NAO ALTERE O TRECHO ABAIXO
def main():
    n = int(input("Tamanho: "))
    sequencia = []
    
    while n > 0:
        n = n - 1
        num = int(input("Numero: "))
        sequencia.append(num)
        
    sequencia2 = unicos(sequencia)
    print("Sequencia sem duplicatas: ")
    for num in sequencia2:
        print(num, end = ' ')    

if __name__ == '__main__':
    main()