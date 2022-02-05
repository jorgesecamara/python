#Dados um inteiro n > 1 e uma sequência com n números inteiros, verificar se a sequência é uma progressão geométrica (PG). Exibir True se sequência for PG e False caso contrário.
#Uma sequência x1,…,xn
# é uma PG se existe r tal que xk/xk−1=r para todo k=2,…,n
#Exemplos:
#    A sequência 1, 2, 4, 8, 16 é uma PG.
#    A sequência 1, 2, 4, 6, 8 não é uma PG.

n = int(input("Tamanho da sequencia (n > 2): "))
seq = []
while n > 0:
    seq.append(int(input('Digite um numero: ')))
    n -= 1
c = seq[1]/seq[0]
for k, v in enumerate(seq):
    if k > 0:
        if seq[k]/seq[k-1] == c:
            pg = True
        else:
            pg = False
print(pg)


