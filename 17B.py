#Dados n>0 e uma sequência com n números reais, escreva um programa que conta e imprime o número de vezes que cada número ocorre na sequência. 
#Exemplo:
#Digite n: 6
#Digite um numero: 1.0
#Digite um numero: 1.0
#Digite um numero: 1.0
#Digite um numero: 3.1
#Digite um numero: 3.1
#Digite um numero: 5.2
#1.0 aparece 3 vezes
#3.1 aparece 2 vezes
#5.2 aparece 1 vez

n = int(input("Digite n: "))
# inicialmente dicionario de numeros esta vazio
contagem = {}
# leia n numeros e os insira no dicionario
# (valor associado nao e' relevante)
for i in range(n):
    numero = float(input("Digite um numero: "))
    # FAZER:
    # Verificar se numero esta em dicionario
    if f'{numero}' not in contagem.keys():
        contagem[f'{numero}'] = 1
    else:
        contagem[f'{numero}'] += 1
    # e inseri-lo caso contrario
    
# Exibir no. de ocorrencias de cada numero
for k, v in contagem.items():
    print(f'{k} aparece {v}')
