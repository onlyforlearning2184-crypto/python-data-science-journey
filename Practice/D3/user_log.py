index = 1

while True:
    user_input = input("Enter a word: ")

    if user_input == "exit":
        break

    with open("user_log.txt", "a") as f:
        f.write(f"{index}: {user_input}\n")

    index += 1
