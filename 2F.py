    #Em 1882 o matemático Julius Christian Johannes Zeller publicou um algoritmo para calcular o dia da semana de uma data qualquer no formato d/m/a, conhecido hoje por Congruência de Zeller.
    #s=(d+⌊(13∗(m+1))/5⌋+a+⌊a/4⌋−⌊a/100⌋+⌊a/400⌋)mod7
    #Na fórmula acima  ⌊x⌋
    #denota a função piso de x , ou seja, o maior inteiro menor que x . Em python, podemos obter o resultado da função piso usando divisão inteira ( // ). Para fórmula funcionar os meses de janeiro e fevereiro devem ser considerados como meses 13 e 14, respectivamente, do ano anterior. Por exemplo, para calcular o dia da semana corresponde a 3/2/2021 usamos d=3,m=14,a=2020
    #O valor de s
    #indica o dia da semana de acordo com a seguinte conversão

#        Domingo: 1
#        Segunda-feira: 2
#        Terça-feira: 3
#        Quarta-feira: 4
#        Quinta-feira: 5
#        Sexta-feira: 6
#        Sábado: 0
#    Teste para ver que 9/8/1967 e 3/2/2021 caíram em quartas-feiras.
#    Escreva um programa que recebe uma data e determina o dia da semana correspondente usando a Congruência de Zeller. O programa deve ler a data na ordem dia, mês e ano assumindo que o usuário fez a correção acima (janeiro e fevereiro contam como meses 13 e 14 do ano anterior).
#    Por exemplo, dado
#    dia:  7
#    mes:  4
#    ano:  2021
#    o programa deve exibir
#    4
#    indicando que o dia caiu numa quarta-feira.

# Ler data
dia = int(input("dia: ")) 
mes = int(input("mes: "))
ano = int(input("ano: "))
# Calcular dia da semana
dia_da_semana = int(dia + ((13*(mes+1))//5) + ano + (ano//4) - (ano//100) + (ano//400)) % 7
# Exibir resposta
print( dia_da_semana ) 