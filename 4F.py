#    A Congruência de Zeller calcula o dia da semana s
 #   de uma data d/m/a através da fórmula:
  #  s=(d+⌊(13∗(m+1))/5⌋+a+⌊a/4⌋−⌊a/100⌋+⌊y/400⌋)mod7
   # A fórmula supões que os meses de janeiro (1) e fevereiro (2)  são representados como os meses 13 e 14, respectivamente do ano anterior. Por exemplo, 1/2/2020 é representado como 1/14/2019.
    #O valor de s
    #indica o dia da semana de acordo com a seguinte conversão
    #    Domingo: 1
    #    Segunda-feira: 2
    #    Terça-feira: 3
    #    Quarta-feira: 4
    #    Quinta-feira: 5
    #    Sexta-feira: 6
    #    Sábado: 0
    #Escreva um programa que recebe uma data e determina o dia da semana correspondente usando a Congruência de Zeller. O programa deve ler a data na ordem dia, mês e ano  e deve realizar a correção para os meses de janeiro e fevereiro como mencionado acima.
    #Por exemplo, dado
    #dia:  23
    #mes:  2
    #ano:  1855
    #o programa deve exibir
    #6
    #indicando que o dia caiu numa sexta-feira.

# Ler data
dia = int(input("dia: ")) 
mes = int(input("mes: "))
ano = int(input("ano: "))
if mes == 1 or mes == 2:
    mes += 12
    ano -= 1
# Calcular dia da semana
dia_da_semana = (dia + 13 * (mes+1) // 5 + ano + ano // 4 - ano // 100 + ano //400) % 7

# Exibir resposta
print( dia_da_semana ) 