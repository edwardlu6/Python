cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 'King of Spades', 'Queen of Spades', 'Jack of Spades']

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, [1,11], 10, 10, 10]

import random
import sys

card1 = cards[random.randint(0,len(cards) - 1)]
card2 = cards[random.randint(0,len(cards) - 1)]
list = [card1, card2]
list_value1 = 0
list_value2 = 0



if values[cards.index(card1)] != [1, 11] and values[cards.index(card2)] != [1, 11]:
    print('Player hand:', list, values[cards.index(card1)] + values[cards.index(card2)])
    list_value1 += values[cards.index(card1)] + values[cards.index(card2)]
    list_value2 += values[cards.index(card1)] + values[cards.index(card2)]


else:
    if values[cards.index(card1)] == [1, 11] or values[cards.index(card2)] == [1, 11]:
        if values[cards.index(card1)] == [1, 11] and values[cards.index(card2)] == [1, 11]:
            print('Player hand:', list, values[cards.index(card1)][0] + values[cards.index(card2)][0], 'or', values[cards.index(card1)][1] + values[cards.index(card2)][1])
            list_value1 = values[cards.index(card1)][0] + values[cards.index(card2)][0]
            list_value2 = values[cards.index(card1)][1] + values[cards.index(card2)][1]
        elif values[cards.index(card1)] == [1, 11]:
            print('Player hand:', list,  values[cards.index(card1)][0] + values[cards.index(card2)], 'or', values[cards.index(card1)][1] + values[cards.index(card2)])
            list_value1 = values[cards.index(card1)][0] + values[cards.index(card2)]
            list_value2 = values[cards.index(card1)][1] + values[cards.index(card2)]
            if list_value2 == 21:
                print('You got Blackjack!  You win!')
                sys.exit()


        elif values[cards.index(card2)] == [1, 11]:
            print('Player hand:', list,  values[cards.index(card1)] + values[cards.index(card2)][0], 'or', values[cards.index(card1)] + values[cards.index(card2)][1])
            list_value1 = values[cards.index(card1)] + values[cards.index(card2)][0]
            list_value2 = values[cards.index(card1)] + values[cards.index(card2)][1]
            if list_value2 == 21:
                print('You got Blackjack!  You win!')
                sys.exit()

            


choice = input('(h)it or (s)tand? ')
if choice == 'h':
    while True:
        card3 = cards[random.randint(0,len(cards) - 1)]
        print('You drew', card3)
        list += [card3]
        if values[cards.index(card3)] != [1,11]:
            list_value1 += values[cards.index(card3)]
            list_value2 += values[cards.index(card3)]
            if list_value1 == list_value2:
                print('Player hand:', list, list_value1)
            else:
                print('Player hand:', list, list_value1, 'or', list_value2)
        elif values[cards.index(card3)] == [1,11]:
            list_value1 += values[cards.index(card3)][0]
            list_value2 += values[cards.index(card3)][1]
            print('Player hand:', list, list_value1, 'or', list_value2)
        if list_value1 == 21 or list_value2 == 21:
            print('You got Blackjack!  You win!')
            break
        elif list_value1 > 21:
            print('Bust!')
            print('Computer Wins!')
            break
        choice2 = input('(h)it or (s)tand? ')
        if choice2 == 'h':
            continue
        elif choice2 == 's':
            while True:
                if values[cards.index(card1)] != [1, 11] and values[cards.index(card2)] != [1, 11]:
                    print('Computer hand:', list, values[cards.index(card1)] + values[cards.index(card2)])
                    list_value1 += values[cards.index(card1)] + values[cards.index(card2)]
                    list_value2 += values[cards.index(card1)] + values[cards.index(card2)]

                else:
                    if values[cards.index(card1)] == [1, 11] or values[cards.index(card2)] == [1, 11]:
                        if values[cards.index(card1)] == [1, 11] and values[cards.index(card2)] == [1, 11]:
                            print('Computer hand:', list, values[cards.index(card1)][0] + values[cards.index(card2)][0], 'or', values[cards.index(card1)][1] + values[cards.index(card2)][1])
                            list_value1 = values[cards.index(card1)][0] + values[cards.index(card2)][0]
                            list_value2 = values[cards.index(card1)][1] + values[cards.index(card2)][1]
                        elif values[cards.index(card1)] == [1, 11]:
                            print('Computer hand:', list,  values[cards.index(card1)][0] + values[cards.index(card2)], 'or', values[cards.index(card1)][1] + values[cards.index(card2)])
                            list_value1 = values[cards.index(card1)][0] + values[cards.index(card2)]
                            list_value2 = values[cards.index(card1)][1] + values[cards.index(card2)]
                        elif values[cards.index(card2)] == [1, 11]:
                            print('Computer hand:', list,  values[cards.index(card1)] + values[cards.index(card2)][0], 'or', values[cards.index(card1)] + values[cards.index(card2)][1])
                            list_value1 = values[cards.index(card1)] + values[cards.index(card2)][0]
                            list_value2 = values[cards.index(card1)] + values[cards.index(card2)][1]
                while True:
                    card3 = cards[random.randint(0,len(cards) - 1)]
                    print('Computer drew', card3)
                    list += [card3]
                    if values[cards.index(card3)] != [1,11]:
                        list_value1 += values[cards.index(card3)]
                        list_value2 += values[cards.index(card3)]
                        if list_value1 == list_value2:
                            print('Computer hand:', list, list_value1)
                        else:
                            print('Computer hand:', list, list_value1, 'or', list_value2)
                    elif values[cards.index(card3)] == [1,11]:
                        list_value1 += values[cards.index(card3)][0]
                        list_value2 += values[cards.index(card3)][1]
                        print('Computer hand:', list, list_value1, 'or', list_value2)
                    if list_value1 == 21 or list_value2 == 21:
                        print('Computer got Blackjack!  Computer win!')
                        break
                    elif list_value1 > 21:
                        print('Bust!')
                        print('Player Wins!')
                        break
                    break
                break
            break

elif choice == 's':
    card1 = cards[random.randint(0,len(cards) - 1)]
    card2 = cards[random.randint(0,len(cards) - 1)]
    list = [card1, card2]
    list_value1 = 0
    list_value2 = 0
    if values[cards.index(card1)] != [1, 11] and values[cards.index(card2)] != [1, 11]:
        print('Computer hand:', list, values[cards.index(card1)] + values[cards.index(card2)])
        list_value1 += values[cards.index(card1)] + values[cards.index(card2)]
        list_value2 += values[cards.index(card1)] + values[cards.index(card2)]

    else:
        if values[cards.index(card1)] == [1, 11] or values[cards.index(card2)] == [1, 11]:
            if values[cards.index(card1)] == [1, 11] and values[cards.index(card2)] == [1, 11]:
                print('Computer hand:', list, values[cards.index(card1)][0] + values[cards.index(card2)][0], 'or', values[cards.index(card1)][1] + values[cards.index(card2)][1])
                list_value1 = values[cards.index(card1)][0] + values[cards.index(card2)][0]
                list_value2 = values[cards.index(card1)][1] + values[cards.index(card2)][1]
            elif values[cards.index(card1)] == [1, 11]:
                print('Computer hand:', list,  values[cards.index(card1)][0] + values[cards.index(card2)], 'or', values[cards.index(card1)][1] + values[cards.index(card2)])
                list_value1 = values[cards.index(card1)][0] + values[cards.index(card2)]
                list_value2 = values[cards.index(card1)][1] + values[cards.index(card2)]
            elif values[cards.index(card2)] == [1, 11]:
                print('Computer hand:', list,  values[cards.index(card1)] + values[cards.index(card2)][0], 'or', values[cards.index(card1)] + values[cards.index(card2)][1])
                list_value1 = values[cards.index(card1)] + values[cards.index(card2)][0]
                list_value2 = values[cards.index(card1)] + values[cards.index(card2)][1]
    while True:
        card3 = cards[random.randint(0,len(cards) - 1)]
        print('Computer drew', card3)
        list += [card3]
        if values[cards.index(card3)] != [1,11]:
            list_value1 += values[cards.index(card3)]
            list_value2 += values[cards.index(card3)]
            if list_value1 == list_value2:
                print('Computer hand:', list, list_value1)
            else:
                print('Computer hand:', list, list_value1, 'or', list_value2)
        elif values[cards.index(card3)] == [1,11]:
            list_value1 += values[cards.index(card3)][0]
            list_value2 += values[cards.index(card3)][1]
            print(list, list_value1, 'or', list_value2)
        if list_value1 == 21 or list_value2 == 21:
            print('Computer got Blackjack!  Computer win!')
            break
        elif list_value1 > 21:
            print('Bust!')
            print('Player Wins!')
            break
  

