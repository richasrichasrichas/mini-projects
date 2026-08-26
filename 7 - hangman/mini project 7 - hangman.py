# LIBRARIES
import random
import pathlib

# ABRE O ARQUIVO DA LISTA DO DICIONÁRIO
def nome_aleatório():
    import csv
    with open(r'C:\Users\ricar\OneDrive\Desktop\mini projects\7 - hangman\br-sem-acentos.csv'):
        reader = csv.reader('br-sem-acentos.csv', delimiter = " ", quotechar = '|')
        data = list(reader)
        for column in reader:
            random.choice(br-sem-acentos.csv)

print(nome_aleatório())