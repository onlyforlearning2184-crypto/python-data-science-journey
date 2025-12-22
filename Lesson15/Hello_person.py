def hello(name, lang):
    greeting = {
        "English": "Hello",
        "Hindi": "Namaste",
        "Gujrati": "Jai sree krisna",
    }
    msg = f"{greeting[lang]} {name}"
    print(msg)


if __name__ == "__main__":
    import argparse

    parse = argparse.ArgumentParser(description="Provide a personal greeting.")

    parse.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person to greet.",
    )
    parse.add_argument(
        "-l",
        "--lang",
        metavar="language",
        required=True,
        choices=["English", "Hindi", "Gujrati"],
        help="The language of the greeting",
    )
    args = parse.parse_args()
    hello(args.name, args.lang)
