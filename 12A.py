#Dada uma sequência de n > 0 números inteiros, imprimi-la eliminando as repetições.
n = int(input("Digite n: "))
# inicialmente a lista de numeros esta vazia
lista = []
# leia n numeros e os coloque na lista apenas
# se ele ja' nao ocorrer na lista
while n > 0:
    n = n - 1
    numero = int(input("Digite um numero: "))
    # FAZER:
    # Verificar se numero esta em lista
    if numero not in lista:
        lista.append(numero)
    # e inseri-lo caso contrario
    
# Exibir numeros em lista
for c in lista:
    print(c, end=' ')