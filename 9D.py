#Os códigos de barra utilizados para identificarem produtos no Brasil em geral seguem o padrão EAN13. Nesse padrão, o código é formado por 12 dígitos mais um dígito verificador que tem a função de detectar falhas na leitura do código.
#Código de barras no formato EAN13
#Seja d1d2d3d4d5d6d7d8d9d10d11d12
#os 12 primeiros dígitos de um número de código de barras. O dígito verificador d13
#é tal que a seguinte expressão seja múltiplo de 10:
#d1+3d2+d3+3d4+d5+3d6+d7+3d8+d9+3d10+d11+3d12+d13
#Por exemplo, o código de barras na figura acima (5 901234 12345 7) satisfaz 
#(5 + 3*9 + 0 + 3*1 + 2 + 3*3 + 4 + 3*1 + 2 + 3*3 + 4 + 3*5 + 7) % 10 == 0
#Escreva um programa que recebe um inteiro representando um código de barras e verifica se ele é válido. Seu programa deve conter uma função ean13 que recebe um inteiro e devolve um bool indicando se o código é válido ou não.
#Importante: Seu programa deve chamar a função input fora da função ean13.
#Exemplos:
#    Para n: 5_901234_12345_7, a saída deve ser valido
#    Para n: 5_901234_12345_5, a saída deve ser invalido

def ean13(codigo) -> bool:
    n = str(codigo)
    if (int(n[0])+3*int(n[1])+int(n[2])+3*int(n[3])+int(n[4])+3*int(n[5])+int(n[6])+3*int(n[7])+int(n[8])+3*int(n[9])+int(n[10])+3*int(n[11])+int(n[12])) % 10 == 0:
        return print('valido')
    else:
        return print('invalido')
    '''
    Verifica se codigo e' de barras e' valido.
    Devolve True ou False.
    '''
    # Implementar

def main():
    '''
    Recebe um inteiro do usuario e verifica se e' codigo de barras valido.
    '''
    # Escrever seu programa aqui, alinhado a linha acima
    n = int(input("Digite n: "))
    # n = n.replace(' ', '')
    # n = int(n)
    return ean13(n)
    # print(ean13(n))
    # seu programa nao deve conter nada fora de funcoes
    # Seu programa deve chamar a funcao ean13
    
# NAO ALTERAR CODIGO ABAIXO -- Seu programa nao deve conter 
if __name__ == '__main__':
    main()
