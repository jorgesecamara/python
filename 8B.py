#Dado reais x>1 e e>0, encontrar y tal que 10y≈x com erro no máximo e.
#Exemplo: Dado x=3 e e=0.1 retornar qualquer −0.1<10y−x<0.1

x = float(input("x: ")) # x > 1
e = float(input("e: ")) # erro > 0
# encontrar y pelo metodo da bisseccao
# tal que  -erro <= y - log10(x) <= erro
a = 0.0  # limite inferior
b = x    # limite superior
continuar = True
while  (10**b) > (10**a):
    y = (a+b)/2
    if (10**y - x) > e
        continuar = True
        
# while b - a > e and continuar:
#     y = (a+b)/2
#     if (10**y - x) == 0:
#         continuar = False
#     elif (10**y - x) * (10**a - x) > 0:
#         a = y
#     elif (10**y - x) * (10**a - x) < 0:
#         b = y
#     elif b - a <= e:
#         y = (a + b)/2
#         continuar = False
        
print(y)