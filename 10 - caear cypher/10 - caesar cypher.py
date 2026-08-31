import string

letters = string.ascii_lowercase

def encryption(message, shift):
    return "".join([letters[(letters.index(letra) + shift) % len(letters)] for letra in message])

def decryption(message, shift):
    return "".join([letters[(letters.index(letra) - shift) % len(letters)] for letra in message])

print('Welcome to the Caesar Cypher converter!')
menu = input('Do you want to encrypt or decrypt a message?')
valid_input = False
while valid_input == False:
    if menu == 'encrypt':
        try: shift = int(input('What is the value of the shift?'))
        except ValueError: 
            shift = int(input('ValueError. Please use an integer.'))
        message = input('What is the message to encrypt?')
        valid_input = True
        print(encryption(message, shift))
    elif menu == 'decrypt':
        try: shift = int(input('What is the value of the shift?'))
        except ValueError: 
            shift = int(input('ValueError. Please use an integer.'))
        message = input('What is the message to decrypt?')
        valid_input = True
        print(decryption(message, shift))
    else:
        menu = input('Input error, please type "encrypt" or "decrypt" with lowercase letters.') 