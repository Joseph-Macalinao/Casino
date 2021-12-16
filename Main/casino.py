import random
import time

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
                wager(wage, False)
                main()
            elif total == 21:
                print("Congratulations. You won!")
                wager(wage)
                main()
    for i in range(3):
        house += random.choice(cards)
        print(f'House: {house}')
    if house > 21:
        print("Congratulations, you won!")
        wager(wage)
        main()
    elif house == 21 and total != 21:
        print('Sorry, you lose...')
        wager(wage, False)
        main()
    elif house < total:
        print('Congratulations, you won!')
        wager(wage)
        main()
    elif house > total:
        print('Sorry, you lose...')
        wager(wage)
        main()
    elif house == total:
        print("Tie, go again!")
        twenty_one()


def coin():
    hot = True
    while hot:
        h_o_t = input("Heads or Tails [H/T]\n")
        if h_o_t.upper() not in ['H', 'T']:
            print("Input must be H or T")
        else:
            break
    wage = int(input("How much would you like to bet?"))
    flip = random.randint(1, 2)
    print("Flipping...")
    time.sleep(4)
    if flip == 1:
        print("It's heads")
    else:
        print("It's tails")
    if flip == 1 and h_o_t.upper() == 'H':
        print('Congrats, you won!')
        wager(wage)
        main()
    elif flip == 1 and h_o_t.upper() == 'T':
        print('Sorry, you lose...')
        wager(wage, False)
        main()
    elif flip == 2 and h_o_t.upper() == 'T':
        print('Congrats, you won!')
        wager(wage)
        main()
    elif flip == 2 and h_o_t.upper() == 'H':
        print('Sorry, you lose...')
        wager(wage, False)
        main()


def roulette():
    pass


def wager(bet: float, win=True):
    '''
    used in all games to used for the winnings and the betting
    :param bet: how much they are betting
    :return:
    '''
    if win:
        print(f'You won ${bet * 2}')
        return bet * 2
    else:
        print(f'You lose all your bet')
        return 0



def main():
    time.sleep(3)
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
