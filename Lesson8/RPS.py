import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


play_again = True

while play_again:

    print("")
    player_Choice = input("Enter...\n1 for Rock.\n2 for Paper.\n3 for Scissors. \n\n>")

    player = int(player_Choice)
    if player < 1 or player > 3:
        sys.exit("your enter the wrong number...\nChoose from 1,2 or 3.")

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

    play_again = input("\nPlay again? \nY for Yes or\nQ to quit\n\n").strip().upper()
    if play_again == "Y":
        continue
    else:
        print("\n🙏🙏🙏🙏")
        print("Thank you for playing!\n")
        sys.exit("Bye! 🙋‍♂️🙋‍♂️")
        # break
