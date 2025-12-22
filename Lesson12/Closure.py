def parent_func(person, coins):
    # coins = 10

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left. ")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left. ")
        else:
            print("\n" + person + " is out of coins. ")

    return play_game


rachit = parent_func("Rachit", 10)
krupa = parent_func("Krupa", 3)


rachit()
rachit()
rachit()
rachit()


krupa()
