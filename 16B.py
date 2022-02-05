#Escreva um programa que lê o nome de um arquivo e exibe apenas as linhas do arquivo de texto correspondente que não iniciam com #. Teste com o arquivo chamado notas2.txt cujo conteúdo é
# Este arquivo contem as notas de alguns alunos
# Formato: NUSP NOTA
#10056789 7.5
#10104521 6.3
#09126349 5.8
#11023934 9.1
# Lembrete: corrigir as notas abaixo
#10234981 8.9
#10238797 3.4
# Fim da lista de notas

nome = input("Nome do arquivo: ") # <- nao modificar essa linha
# exibir linhas que nao comecem por '#'
with open(nome) as arquivo:
    for linha in arquivo:
        if linha[0] != '#':
            print(linha, end='')