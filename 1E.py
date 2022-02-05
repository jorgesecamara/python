from math import sqrt # precisamos disso para usar a funcao sqrt

a = 1
b = -3
c = 2
x1 = sqrt(2)    # Usar formula de Baskhara: x1 = (-b  - sqrt(b**2 - 4*a*c))/(2*a)
x2 = sqrt(9)    # x2 = (-b  + sqrt(b**2 - 4*a*c))/(2*a)
print( x1, x2 )  # exibir as raizes do polinomio com x1 < x2