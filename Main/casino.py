def twenty_one():
    pass

def coin():
    pass

def main():
    games = ['21', 'C']
    print("Welcome to Macalinao Chips, the best fake online Python-based Casino ever,  "
          "\nhow may we serve you today?")
    while True:
        game_deci = input("21: BlackJack\nC: Coin Flip\n")
        if game_deci.upper() in games:
            break
        print("Sorry, not an option...")

    if game_deci.upper() == 'C':
        coin()
    else:
        twenty_one()







if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
