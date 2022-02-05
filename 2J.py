#Escreva um programa que recebe dois inteiros do usuário e exibe True se um deles divide o outro e False caso contrário.

#Por exemplo:
#
 #   Para 6 e 3 o programa exibe True
  #  Para 3 e 6 o programa exibe True
   # Para 5 e 7 o programa exibe False
    #Para 4 e 1 o programa exibe True

primeiro = int( input("Digite um numero inteiro: "))
segundo = int( input("Digite outro numero inteiro: "))

resto = primeiro % segundo #% segundo
resto2 = segundo % primeiro #% primeiro

divisao = True
if resto == 0 or resto2 == 0:
    print(divisao)
else:
    divisao = False
    print(divisao)

    
#elif resto >= 0:
#    divisão = False
#    print(divisao)
#elif resto != 0:
#    divisão = False
#    print(divisao)

#if resto == 0:
#    print(divisao)
#if resto2 == 0:
#    print(divisao)
#else: #if resto != 0:
#    divisao = False
#    print(divisao)

#rola_div = True
#while resto == 0 or resto2 ==0:
#    print(rola_div)
#    if resto != 0 or resto2 != 0:
#        rola_div = False 
 #   if resto >= 0 or resto2 >=0:
#        rola_div = False 
#            
#print(rola_div) 

#if resto == 0: # or resto2 == 0:
#    print(rola_div)
#elif resto != 0: # or resto2 != 0:
#    rola_div = False
#elif resto <= 0: # or resto2 <= 0:
#    rola_div = False
#if resto >= 0: # or resto2 >= 0:
#    rola_div = False