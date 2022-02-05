#Escreva uma função binomial(m,n) que recebe dois inteiros não-negativos m e n e devolve o número de combinações de m n-a-n, ou seja m!/[(m-n)!n!]
#Exemplos:
#    binomial(1,1) = 1
#    binomial(3,2) = 3
#    binomial(0,0) = 1
#    binomial(5,2) = 10

def fatorial(n: int) -> int:
    " Recebe um inteiro n >= 0 e devolve n! "
    # fazer
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return int(f)
    
def binomial(m: int, n: int) -> int:
    " Recebe inteiros m,n >= 0 e devolve m!/((m-n)!n!)"
    # fazer
    comb = fatorial(m) / (fatorial((m-n)) * fatorial(n))
    return int(comb)
s = 0
c = 0

print(binomial(s,c))
    
    

