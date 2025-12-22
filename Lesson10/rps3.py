import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSOR = 3

    print("")
    player_Choice = input("Enter...\n1 for Rock.\n2 for Paper.\n3 for Scissors. \n\n>")
    if player_Choice not in ["1", "2", "3"]:
        print("your enter the wrong number...\nChoose from 1,2 or 3.")
        return play_rps()

    player = int(player_Choice)
    computer_Choice = random.choice("123")
    computer = int(computer_Choice)
    print("")
    print("you chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Computer chose " + str(RPS(computer)).replace("RPS.", "") + ".")
    print("")

    if player == 1 and computer == 3:
        print("👌😜You win!")

    elif player == 2 and computer == 1:
        print("👌😜You win!")

    elif player == 3 and computer == 2:
        print("👌😜You win!")

    elif player == computer:
        print("It's a 👔Tie!")

    else:
        print("😱😱You loss!")

    print("\nPlay again?")
    while True:
        play_again = input(" \nY for Yes or\nQ to quit\n").strip().upper()
        if play_again not in ["Y", "Q"]:
            continue
        else:
            break

    if play_again == "Y":
        return play_rps()
    else:
        print("\n🙏🙏🙏🙏")
        print("Thank you for playing!\n")
        sys.exit("Bye! 🙋‍♂️🙋‍♂️")
        # break


play_rps()
