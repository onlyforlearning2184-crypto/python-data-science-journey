import Guess_number as gn
import Rps8 as rps
import sys


def choose(name="PlayerOne"):
    welcome_back = False
    while True:
        if welcome_back == True:  # noqa: E712
            print(f"{name}, welcome back to the Arcade menu.")
        # else:
        #     print(f"{name}, welcome back to the Arcade! 🤖")
        playerchoice = input(
            "Please choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press 'x' to exit the Arcade\n\n"
        )
        if playerchoice not in ["1", "2", "x"]:
            print(f"{name}, please enter 1, 2 , or x.")
            return choose(name)

        welcome_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps.rps(name)
            rock_paper_scissors()

        elif playerchoice == "2":
            guess_my_number = gn.GN(name)
            guess_my_number()
        else:
            print("\nSee your next time!\n")
            sys.exit(f"Bye, {name}! 👋")


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
    print(f"{args.name}, welcome back to the Arcade! 🤖")
    choose(args.name)
