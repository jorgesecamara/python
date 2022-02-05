#Dado um inteiro a0, calcule o valor a1 obtido pela soma de seus dígitos, e a soma a2 dos dígitos de a1 e assim por diante até encontrar an<10,  ou seja, um número com um único dígito. O número n de iterações até terminar esse processo é chamado de persistência aditiva de a0
#Por exemplo, para a0=9876
#temos a1=30 e a2=3, portanto 9876 possui persistência aditiva 2
#Calcule a persistência aditivia de um dado n>0


n = int(input("n: "))
n1 = n
resultado = 0
while not (len(str(n)) == 1):
    acumulado = 0
    for i in str(n):
        acumulado += int(i)
    resultado += 1 
    n = acumulado
print(resultado)
