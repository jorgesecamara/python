numero = int( input("Digite um numero primo: "))
# verificar se numero e' soma de dois quadrados usando o Teorema de Fermat

eh_primo = True
if numero % 4 == 1:
    print(eh_primo)
elif numero % 4 >= 1: 
    eh_primo = False
    print(eh_primo)
#i = 2 
#while eh_primo and (i<numero):
#    eh_primo = (numero % i != 0)
#    i = i + 1 

print (eh_primo)
#                                eh_primo = True 
 #                               divisor = 2 
  #                              while divisor < numero and eh_primo:
   #                                 if numero % divisor == 0:
    #                                    eh_primo = False
     #                               divisor += 1 
      #                          
       #                         if eh_primo and numero != 1:
        #                            eh_primo = True
         #                       else:
          #                          eh_primo = False
#
#d = 2 
#while d < numero:
#    if numero%d == 0:
#        eh_primo = False
#    d += 1
#    
#if numero <= 1:
#    eh_primo = False

    #if eh_primo:
    #    print(True)
    #else:
    #    print(False)

#eh_primo = True
#i = 2
#while eh_primo and (i < numero):
#    eh_primo = (numero % i != 0)
#    i = i + 1
