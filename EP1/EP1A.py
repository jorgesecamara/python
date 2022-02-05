# NAO MODIFICAR A LINHA ABAIXO
from testagem import infectado, num_individuos, num_testes, envia

# # MODIFICAR A PARTIR DAQUI
N = num_individuos() # no. total de individuos

resposta = '0' # inteiro representando estado dos individuo tal que: 
             #   digito i = 0: individuo i nao esta infectado
             #   digito i = 1: individuo i esta infectado

# Testagem linear 1:1
i = 0

while i < N:
    resultado = infectado(i)
    print(resultado, i) #, end = ' '
    i = i + 1
    # print(type(resultado))
    resposta += '0' if resultado == False else '1' #  para resultado da funçao infectado(i)  se for False retorna 0 se for True retorna 1

envia(int(resposta,2)) # conversao de binario para inteiro 101010000101010100011100000

# Exibir no. total de testes realizados (deve ser = no. individuos)
# print("Total de testes realizados:", num_testes())
# # Submeter resultados dos testes codificado como inteiro
# print(resposta)
# # resultado = envia(int(resposta,2))
# resultado = envia(resposta)
# print(resultado)
# print(int('10110',2))