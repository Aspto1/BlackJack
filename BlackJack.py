#make a list of cards
#make the computer give you number
#make the a if loop

import time
import random
def player():
    card_1 = random.choice(cards)
    card_2 = random.choice(cards)
    card_3 = 0
    print('drawing....')
    time.sleep(0.5)
    print('These are your cards: ' + str(card_1) +' ' + str(card_2))

    if card_1 in cards_value:
        card_1 = cards_value[card_1]
    if card_2 in cards_value:
        card_2 = cards_value[card_2]

    hit = input('Do you want another card? (yes/no):')
    if hit == 'No'.lower():
        card_3 = 0
    elif hit == 'yes'.lower():
        card_3 = random.choice(cards)
        if card_3 in cards_value:
            card_3 = cards_value[card_3]
    if card_3 == 0:
        pass
    else:
        print('')
        print('Player: ' + str(card_1) + ' ' + str(card_2) + ' ' + str(card_3))

    time.sleep(1)

    card_1 = int(card_1)
    card_2 = int(card_2)
    card_3 = int(card_3)

    sum = card_1 + card_2 + card_3
    print('Player score is :' + str(sum))

    return sum



def computer():
    import random
    import time

    card_1 = random.choice(cards)
    card_2 = random.choice(cards)
    card_3 = 0
    print('Computer drawing.....')
    time.sleep(0.5)
    print('Computer: ' + str(card_1) + ' ' + str(card_2))

    if card_1 in cards_value:
        card_1 = cards_value[card_1]
    if card_2 in cards_value:
        card_2 = cards_value[card_2]
    sum = card_1 + card_2

    if sum  <= 10 or sum <= 15:
        card_3 = random.choice(cards)
        if card_3 in cards_value:
            card_3 = cards_value[card_3]
    elif sum >= 17:
        card_3 = 0
        if card_3 in cards_value:
            card_3 = cards_value[card_3]
    if card_3 == 0:
        pass
    else:
        print('Computer: ' + str(card_1) + ' ' + str(card_2) + ' ' + str(card_3))
    time.sleep(1)
    card_1 = int(card_1)
    card_2 = int(card_2)
    card_3 = int(card_3)
    sum = card_1 + card_2 + card_3

    print('Computer score is :' + str(sum))
    return sum





print('This is Black Jack or 21')
starter = input('Do you want to play blackjack: (yes/no): ')
if starter != 'yes'.lower():
    exit
else:
    print('starting game')
time.sleep(1)


cards = [2,3,4,5,6,7,8,9,10,'J','K','Q','A']
cards_value = {'J':10,'K':10,'Q':10,'A':1}

player_sum = player()

computer_sum = computer()
if player_sum > 21:
    print('Computer lost')
    exit
elif player_sum == 21:
    print('player won')
    exit
else:
    pass




if player_sum > computer_sum:
    print('Player won')
elif computer_sum > player_sum:
    print('Computer won')
elif computer_sum == player_sum:
    print('Tie')
