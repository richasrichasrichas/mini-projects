import string

letters = string.ascii_lowercase
shift = int(input('What is the value of the shift?'))

def encryption(message):
    letra = 'd'
    posicao = letters.index(letra)
    nova_posicao = (posicao + shift) % len(letters)
    nova_letra = letters[nova_posicao]
    return [message.count in letters for shift in message]

def decryption(message, shift):
    return [message.index(letters) in letters in message + shift]

print('Welcome to the Caesar Cypher converter!')
menu = input('Do you want to encrypt or decrypt a message?')
valid_input = False
while valid_inputalid_input == False:
    if menu == 'encrypt':
        valid_inputalid_input = True
        encryption()
    elif menu == 'decrypt':
        valid_input = True
        decryption()
    else:
        print('Input error, please use lowercase letters.')