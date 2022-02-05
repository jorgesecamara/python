#Escreva um programa estruturado que recebe do usuário um inteiro n > 0 e uma lista de n números inteiros e os exibe na ordem inversa de entrada.
#Exemplo: 
#Para n = 3 e a sequência de entrada 3 42 105 o programa deve exibir 105 42 3
#Cada número deve ser exibido em uma linha distinta.
def main():
    # Escreva seu programa aqui
    n = int(input('numero de lançamento: '))
    numero = []
    resp = []
    while n > 0:
        numero.append(int(input("Numero: ")))
        n = n - 1
    s = numero[::-1]
    for c in s:
        print(c)
    # numero.sort(reverse=True)
    # for c in numero:
    #     print(c)
    
    
# NAO MODIFIQUE A LINHA ABAIXO
if __name__ == "__main__":
    main()