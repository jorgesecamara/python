#Dados inteiros n > 1 e  m > 1, calcular o máximo divisor comum deles (mdc). O máximo divisor comum é o maior inteiro que divide ambos os números.
#Exemplos:
#
#    mdc(9,12) = 3.
#    mdc(15,24) = 3.
#    mdc(7,5) = 1.
m = int(input("Digite m: "))
n = int(input("Digite n: "))
mdc = n
while n % mdc != 0 or m % mdc != 0:
    mdc = mdc - 1
    
#mdc = m # tentativa inicial
#while "mdc nao dividir m ou n":
# mdc = mdc - 1
# exbir resultado    
print( mdc )