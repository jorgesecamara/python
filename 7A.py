#Escreva um programa que lê um número inteiro n > 1 e uma sequência de n inteiros e determina o maior divisor comum dos números da sequência.
#Exemplo: 
#Para a sequência 3 42 105 o programa deve exibir 3
#Use a propriedade: mdc(a,b,c)=mdc(mdc(a,b),c).

# n = int(input("Digite n: "))
# while n > 0:
#     numero = int(input("Numero: "))
#     n = n - 1
def __mdc_(x, y):
    while(y):
        x, y = y, x % y
    return x

def mdc(nums):
    if len(nums) == 2:
        return __mdc_(nums[0], nums[1])
    else:
        mdc_val = __mdc_(nums[0], nums[1])
        nums[0] = mdc_val
        del nums[1]
        return mdc(nums)
        
n = int(input("Digite n: "))
numero = [] 
while n > 0:
    numero.append(int(input('Numero: ')))
    n = n - 1
numero.sort()
print(mdc(numero))