# LIBRARIES
import random
import pandas

# ABRE O ARQUIVO DA LISTA DO DICIONÁRIO
def nome_aleatório():
    import csv
    with open('br-sem-acentos.csv', newline = '') as csvfile:
        spamreader = csv.reader('br-sem-acentos.csv', delimiter = ' ', quotechar = '|')
        for row in spamreader:
            print(', '.join(row))
