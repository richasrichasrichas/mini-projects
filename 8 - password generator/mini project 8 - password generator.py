import random
characters=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ç', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols=['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+', '§', '|', '<', '>', ';', ':', ',', '.', '/', '?', '°']

print('Welcome to the password generator.')
nr_letters = int(input(f'How many letters would you like?'))
nr_symbols = int(input(f'How many symbols would you like?\n'))
nr_numbers = int(input(f'How many numbers would you like?\n'))

password = ''

for char in range(1, nr_letters + 1):
    password += random.choice(characters)


for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)


for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(''.join(random.sample(password, len(password))))