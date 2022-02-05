#Escreva um programa que lê o conteúdo do arquivo de texto notas.txt e exibe suas linhas precedidas pela numeração. Ou seja, seu programa deve exibir (na tela):
#1. 10056789 7.5
#2. 10104521 6.3
#3. 09126349 5.8
#4. 11023934 9.1
#5. 10234981 8.9
#6. 10238797 3.4
#O arquivo "notas.txt" está salvo no servidor quando executando no PACA.

nome = "notas.txt"
with open(nome) as arquivo:
    # alterar para ler linhas do arquivo e exibir linhas precedidas por numeracao
    n = 1
    for linha in arquivo:
        print(str(n)+'.', linha, end='')
        n += 1
      