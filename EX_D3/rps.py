# 🟦 Exercise 14 — Rock-Paper-Scissors (with Score, Loops, and Functions)
import random

player_win = 0
computer_win = 0
tie = 0


def get_computer_choice():
    li = ["rock", "paper", "scissors"]

    return random.choice(li)


def decide_winner(player, computer):
    global player_win, computer_win, tie
    if player == "rock" and computer == "scissors":
        player_win += 1
        return "👌😜You win!"

    if player == "paper" and computer == "rock":
        player_win += 1
        return "👌😜You win!"

    if player == "scissors" and computer == "paper":
        player_win += 1
        return "👌😜You win!"

    if player == computer:
        tie += 1
        return "It's a 👔Tie!"

    computer_win += 1
    return "😱😱You loss!"


while True:
    choice_li = ["rock", "paper", "scissors"]
    player = str(input("Enter your choice or quit : ")).strip().lower()

    if player == "quit":
        break

    if player not in choice_li:
        print("Wrong choice try again!...")
        continue

    computer = get_computer_choice()
    print("Computer chose:", computer)

    print("\n\n")

    game_result = decide_winner(player, computer)
    print(game_result)

print("\nFinal Score:")
print("Player:", player_win)
print("Computer:", computer_win)
