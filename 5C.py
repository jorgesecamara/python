#Dado inteiro n>0, obter e exibir número eliminando ocorrências adjacentes de dígitos.

#Exemplo: Dado 122322441 exibir 123241

n = int(input("Digite n: "))
l = []
for c in str(n):
    l.append(int(c))
for c in l:
        
    for k, v in enumerate(l):
        if k < len(l)-1:
            if l[k] == l[k+1]:
                l.pop(k)
for n in l:
    print(n, end='')
    

# n = int(input("Digite n: "))
# l = []

# for c in str(n):
#     l.append(int(c))
    
# for k, v in enumerate(l):
#     if k < len(l) - 1:
#       if l[k] == l[k+1] or l[k] == l[k-1]:
#             l.pop(k)
            
# for n in l:
#     print(n, end='')