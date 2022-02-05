    # NAO MODIFICAR A LINHA ABAIXO
from testagem import infectados_em, num_individuos, num_testes, envia

# MODIFICAR A PARTIR DAQUI
N = num_individuos()
resposta = '0' # inteiro representando estado dos individuo tal que: 
             #   digito i = 0: individuo i nao esta infectado
             #   digito i = 1: individuo i esta infetcado

# Testagem por particionamento binario
i = 0
resultado = '0'

while i < N:
    print('-'*30)
    print('Iniciando checagem',i)
    print('num_testes',num_testes())

    if N - i >=3 and not infectados_em(i, i + 4 if N - i >= 4 else N - i +1):
        print('igual a 3')
        print(i, i+3 if N - i >= 3 else N - i, 'tres')
        i += 3 if N - i >= 3 else N - i
        resultado += '0'* 3 # if N - i >= 3 else N - i
        continue
    else:
        print('menor que 3')
        for do in range(3):
            if not infectados_em(i,i+1): resultado += '0'
            else: resultado += '1'
            i += 1
            

envia(int(resultado[:-2],2))
