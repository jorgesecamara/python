#Escreva um programa que recebe um número inteiro e exibe True caso o número seja par e False caso contrário. 
#Lembre-se: Um número é par se e somente se o resto da divisão por 2 é zero.
numero = int( input("Digite um numero inteiro: "))

# verificar se numero e' par
eh_par = ((numero % 2) == 0)        # expressao booleana

print(eh_par)