n_auctioners = input('How many auctioners there are?')

auctioners = {
}


def bid_add(name_i, value_i):
    auctioners[name_i] = value_i


while True:
    name_i = input('Whats your name? ')
    value_i = float(input('How much would you like to bid? '))
    bid_add(name_i, value_i)

    more_auctioner = input('Is there another bidder? (yes/no) ').strip().lower()
    while more_auctioner not in ('yes', 'no'):
        more_auctioner = input('Say yes or no: ').strip().lower()

    if more_auctioner == 'no':
        break

winner = max(auctioners, key=auctioners.get)
print(f'Vencedor: {winner}, lance de {auctioners[winner]}')