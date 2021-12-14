import random

cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
        6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
        11, 11, 11, 11, 12, 12, 12, 12]


def twenty_one():
    total = 0
    house = 0
    wage = int(input("How much would you like to bet?"))
    while True:
        hit_or = input("Would you like a hit? N to stop")
        if hit_or.upper() == 'N':
            break
        else:
            hit = random.choice(cards)
            total += hit
            print(total)
            if total > 21:
                print("Sorry, you lose...")
                wager(wage)
                main()
            elif total == 21:
                print("Congratulations. You won!")
                wager(wage)
    for i in range(3):
        house += random.choice(cards)
        print(f'House: {house}')
    if house > 21:
        print("Congratulations, you won!")
        wager(wage)#figure out how to pay player
    elif house == 21 and total != 21:
        print('Sorry, you lose...')
    elif house < total:
        print('Congratulations, you won!')
    elif house > total:
        print('Sorry, you lose...')
    elif house == total:
        print("Tie, go again!")
        twenty_one()

def coin():
    pass


def roulette():
    pass


def wager(bet: float):
    '''
    used in all games to used for the winnings and the betting
    :param bet: how much they are betting
    :return:
    '''
    pass


def main():
    games = ['21', 'C', 'R']
    print("Welcome to Macalinao Chips, the best fake online Python-based Casino ever,  "
          "\nhow may we serve you today?")
    while True:
        game_deci = input("21: BlackJack\nC: Coin Flip\nR: Roulette\n")
        if game_deci.upper() in games:
            break
        print("Sorry, not an option...")

    if game_deci.upper() == 'C':
        coin()
    elif game_deci.upper() == 'R':
        roulette()
    else:
        twenty_one()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
