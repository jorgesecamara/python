from math import sqrt 

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# Usar formula de Baskhara: x = (-b  +- sqrt(b**2 - 4*a*c))/2
#x = (-b +- sqrt(b**2 - 4*a*c))/2

x = (-b +- sqrt(b**2 - 4*a*c))/2
x1 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b + sqrt(b**2 - 4*a*c))/(2*a)

#x1 = (-b - sqrt(b**2 - 4*a*c))/2
#x2 = (-b + sqrt(b**2 - 4*a*c))/2

#x1 = sqrt(2) 
#x2 = sqrt(9)   
print( x1, x2 )  # exibir as raizes do polinomio com x1 < x2