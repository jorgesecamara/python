#Modifique o seguinte programa para que receba um valor inteiro `tempo` do usuário, representando o número de minutos gasto em uma atividade, e o converta em `dias`, `horas` e `minutos` tal que tempo=24∗60∗dias+60∗horas+minutos com horas<24 e minutos<60
#Por exemplo, o valor 
#tempo=4445
#deve ser convertido em
#dias=3
#horas=2
#minutos=5

# Dado tempo em minutos, compute os valores de dias, horas e minutos tais que
#tempo = 24*60*dias + 60*horas + minutos, minutos < 60, horas < 24

tempo = int(input("Tempo: "))

dias = tempo // (24*60)
dias_rest = tempo % (24*60)
horas = ((tempo // 60) % 24)
horas_rest = tempo % 60 
minutos = tempo % 60 


#dias = tempo // (60*24)
#dias_rest = tempo % (60*24)
#horas = (tempo // 60) % dias
#horas_rest = horas % dias_rest
#minutos = dias % horas

#horas = (tempo % 60 % dias)
#minutos = (tempo - dias - horas) 
#dias = int(tempo // (60*24))
#horas = int(tempo % 60 % dias)
#minutos =  tempo % 60 

# Nao modifique a linha abaixo
print( dias, horas, minutos )
 