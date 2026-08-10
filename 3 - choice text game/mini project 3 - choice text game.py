print('Welcome to')
print('''                  _ _                             
                  | | |                            
  __ _  ___   __ _| | | _____  ___ _ __   ___ _ __ 
 / _` |/ _ \ / _` | | |/ / _ \/ _ \ '_ \ / _ \ '__|
| (_| | (_) | (_| | |   <  __/  __/ |_) |  __/ |   
 \__, |\___/ \__,_|_|_|\_\___|\___| .__/ \___|_|   
  __/ |                           | |              
 |___/                            |_|         ''')

input('Press enter to start.')

print('Your name is Marcus Iverson, an English Championship goalkeeper at the Merseyside Ogres F.C.')
input('''                  __,='`````'=/__
                          '//  (o) \( o) \ `'         _,-,
                          //|     ,_)   (`\      ,-'`_,-\
                        ,-~~~\  `'==='  /-,      \==```` \__
                       /        `----'     `\     \       \/
                    ,-`                  ,   \  ,.-\       \
                   /      ,               \,-`\`_,-`\_,..--'\
                  ,`    ,/,              ,>,   )     \--`````\
                  (      `\`---'`  `-,-'`_,<   \      \_,.--'`
                   `.      `--. _,-'`_,-`  |    \
                    [`-.___   <`_,-'`------(    /
                    (`` _,-\   \ --`````````|--`
                     >-`_,-`\,-` ,          |
                   <`_,'     ,  /\          /
                    `  \/\,-/ `/  \/`\_/V\_/
                       (  ._. )    ( .__. )
                       |      |    |      |
                        \,---_|    |_---./
                        ooOO(_)    (_)OOoo''')
print('After you got relegated, this is the chance for you to rise up to the Premier League again with your team.')
input('''  _______
          | _     |
    o     |_o=--  |
   () o
   |\,
''')
print('The match stands 1-0 to your club against your rivals, the Droylsden Butchers, and this is the last strike of the game.')
print('''     ____________        _..._
     | ________ |  ___ .'     `. ____________
     ||        || |   /`.  .-'  \            |
     ||        || |   )X / X.   "\           |
     ||        || |   | (_)     _/           |
     ||________|| |   /((())) / \_____       |
     |        ] | |   \______/  //    \      |
     |          | |   _..-)    //  (\/)\     |
     |          | |  / .\\_..-' \   \/  \    |
     |          | |_/    \       `. Mom  \___|
     |          |  /     |         \     /
_____|__________| /      /         /    / _______
                  |    ./|        /    /
                 _|____\_|        |   /
                 \       /       _)   \__
                  \     /       (_\    \()
               ___|_____|____  / / \\_\/
            __/           |  |/ /___|
    ..'`..'|  |           | _/_/    |       
  .'(( ((( |__|           |(__()    |
.'((( ((( .'__|           |  |______|________
 ((( (( ((`.  |           |  |              /
(((((  (((((`.|           |  |             /
  ((( ((( ((.'|           | /             /
`..-''-....'  |___________|/             /

''')
input('Can you save the game from this shot?')
print('The striker sets it and shoots.')
print('''         
     -   \O                                     ,  .-.___
   -     /\                                   O/  /xx\XXX\
  -   __/\ `                                  /\  |xx|XXX|
     `    \, ()                              ` << |xx|XXX|
 jgs^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
choice1 = input('Which side do you go to block the ball? Type "Left-Up" "Left-Down" "Right-Up" "Right-Down"')
choice2 = input('You defended the kick but it was a rebound! The enemy midfielder is coming to the ball, what do you do? Type "Run at the ball" "Block left" "Block right"') 
choice3 = input('''You bumped into the midfielder and it's a penalty!!! The referee waivers at you the yellow card, so you are still in the field, but this is your last chance, where do you jump to defend the ball? Type "Middle" "Left-Up" "Left-Down" "Right-Up" "Right-Down"''')
valid_choice = False

while valid_choice == False:
  if choice1 == 'Left-Up':
    valid_choice == True
    print('You catched it!! The referee ends the match and the Merseyside Ogres are officially in the Premier League again!!!');
  elif choice1 == 'Right-Down':
    valid_choice == True
    choice2
    if choice2 == 'Run at the ball':
        valid_choice == True
        choice3
        if choice3 == "Middle":
          valid_choice == True
          print('It went out!! The referee ends the match and the Merseyside Ogres are officially in the Premier League again!!!')
        elif choice3 == "Left-Down":
          valid_choice == True
          print('''The dream it's over, the ball went in and the Ogres are in the Championship for another year. GAME OVER''')
        elif choice3 == "Left-Up":
          valid_choice == True
          print('You catched it!! The referee ends the match and the Merseyside Ogres are officially in the Premier League again!!!')
        elif choice3 == "Right-Up":
          valid_choice == True
          print('''The dream it's over, the ball went in and the Ogres are in the Championship for another year. GAME OVER''')
        elif choice3 == "Right-Down":
          valid_choice == True
          print('You catched it!! The referee ends the match and the Merseyside Ogres are officially in the Premier League again!!!')
    elif choice2 == 'Block left':
        valid_choice == True
        print('')
    elif choice1 == 'Left-Down' or 'Right-Up':
      valid_choice == True
      print('')
  else: 
    valid_choice == False
    print('Please choose one of the options.')