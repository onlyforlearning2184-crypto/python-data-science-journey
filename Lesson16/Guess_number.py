import sys
import random


def GN(name="Player_One"):
    game_count = 0
    player_wins = 0

    def play_gn():
        nonlocal name, player_wins

        playerchoice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_gn()

        player = int(playerchoice)
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name}, you chose {player}.")
        print(f"I was thinking about the number {computerchoice}.\n")

        def decide_winner(player, computer):
            nonlocal name, player_wins
            if player == computer:
                player_wins += 1
                return f"🎉{name}, You win!"
            else:
                return f"Sorry, {name}. Better luck next time.  😔😔"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        percentage = (player_wins / game_count) * 100
        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {percentage:.2f}%")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_gn()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye, {name}! 👋")

    return play_gn


if __name__ == "__main__":
    import argparse

    parse = argparse.ArgumentParser(
        description="Provide a personalized game experience."
    )

    parse.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )
    args = parse.parse_args()

    Guess_numb = GN(args.name)
    Guess_numb()
