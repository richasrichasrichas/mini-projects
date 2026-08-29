def calculate_love_score(name1, name2):
    names = (name1 + name2).upper()
    true_l = sum(names.count(letter) for letter in 'TRUE')
    t_love = sum(names.count(letter) for letter in 'LOVE')
    return print(f'{true_l}{t_love}')
    
calculate_love_score('Angela Yu', 'Jack Bauer')