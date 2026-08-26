# LIBRARIES
import random
import pathlib

# ABRE O ARQUIVO DA LISTA DO DICIONÁRIO
def nome_aleatorio():
    import csv
    caminho = r'C:\Users\ricar\OneDrive\Desktop\mini projects\7 - hangman\br-sem-acentos.csv'
    with open(caminho, encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)  # quotechar='"' já é o padrão
        palavras = [linha[0] for linha in leitor if linha]
    return random.choice(palavras)

print(nome_aleatorio())