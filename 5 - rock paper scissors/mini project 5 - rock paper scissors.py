import random

print('welcome to rock paper scissors')
player_op = str(input('what will you play? Type: "Rock", "Paper" or "Scissors"'))
options = ['rock', 'paper', 'scissors']
enemy_option = random.choice(options)

valid_input = False
while valid_input == False:
    if player_op == 'rock' and enemy_option == 'paper':
        valid_input == True
        print('paper beats rock, you lose.')

    elif player_op == 'rock' and enemy_option == 'scissors':
            valid_input == True
            print('rock beats scissors, you win!')

    elif player_op == 'rock' and enemy_option == 'rock':
            valid_input == True
            print('double rock, you draw.')
    if player_op == 'rock' and enemy_option == 'paper':
         valid_input == True
         print('paper beats rock, you lose.')
 
    elif player_op == 'rock' and enemy_option == 'scissors':
             valid_input == True
             print('rock beats scissors, you win!')
 
    elif player_op == 'rock' and enemy_option == 'rock':
             valid_input == True
             print('double rock, you draw.')
             
    if player_op == 'rock' and enemy_option == 'paper':
        valid_input == True
        print('paper beats rock, you lose.')

    elif player_op == 'rock' and enemy_option == 'scissors':
            valid_input == True
            print('rock beats scissors, you win!')

    elif player_op == 'rock' and enemy_option == 'rock':
            valid_input == True
            print('double rock, you draw.')
            
    else:
           valid_input == False
           print('input a valid option.')