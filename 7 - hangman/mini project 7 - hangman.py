import random
import csv

def nome_aleatorio():
    caminho = r'C:\Users\ricar\OneDrive\Desktop\mini projects\7 - hangman\br-sem-acentos.csv'
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        palavras = [linha[0] for linha in leitor if linha]
    return random.choice(palavras)

def jogar():
    palavra_secreta = nome_aleatorio()   # gerada UMA vez, guardada na variável
    vidas = 6
    letras_tentadas = set()

    while vidas > 0:
        # aqui vai a lógica do jogo, usando sempre 'palavra_secreta'
        # ex: mostrar progresso, pedir letra, checar se está em palavra_secreta
        letra = input("Digite uma letra: ").lower()
        letras_tentadas.add(letra)
        print(f'Letras tentadas: {letras_tentadas}')

        if letra not in palavra_secreta:
            vidas -= 1
            print(f"Errou! Vidas restantes: {vidas}")
        
        if all(c in letras_tentadas for c in palavra_secreta):
            print("Você venceu!")
            break

    if vidas == 0:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")
        # aqui a palavra_secreta "morre" junto com a função --
        # quando 'jogar()' termina, a variável local deixa de existir

jogar()