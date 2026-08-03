
print('Welcome to the tip calculator!')
bill=float(input('What was the total bill? $' ))
tip=(float(input('What is the percentage that you want to tip? 10 12 15 '))/100)+1
people=int(input('How much people are paying today?'))
total=float(round((bill/people)*tip, 3))

print(f'The total will be ${total} per person')