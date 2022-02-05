#Uma tripla pitagórica consiste em três inteiros positivos a<b<c tais que a2+b2=c2
#Escreva um programa que encontra (e exibe) a tripla pitagórica tal que a+b+c=1000

# # Encontrar inteiros 0 < a < b < c tais que a*a+b*b = c*c e a+b+c = 1000
# a = 1 # valor inicial
# b = 2 # valor inicial
# c = 3 # valor inicial
# print(a, b, c)
a = []
b = []
c = []
for d in range(1, 500):
    a.append(d)
    b.append(d)
    c.append(d)
for d in a:
    for j in b:
        for k in c:
            if d < j < k and d+ j + k == 1000 and d**2 + j**2 == k**2:
                print(d, j, k)
                
            