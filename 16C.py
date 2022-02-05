Escreva um programa lê um nome de arquivo do usuário e exibe seu conteúdo ignorando comentários. Considere comentário qualquer substring começando com #, mesmo que não seja no início da linha.
Teste com os arquivos chamados notas3.txt e poema.txt (já salvos). Por exemplo, para o arquivonotas3.txt, cujo conteúdo é

nome = input("Nome do arquivo: ") # <- nao altere essa linha
# Escreva seu programa aqui
with open(nome) as arquivo:
    for linha in arquivo:
        if "#" in linha:
            i = linha.index('#')
            print(linha[:i])
        else:
            print(linha, end='')
