# # Number Analyzer
# list_num = []
# for i in range(1, 11):
#     number = int(input("Enter the number : "))
#     list_num.append(number)

# print(list_num)
# print(sum(list_num))
# print(max(list_num))
# print(min(list_num))
# print(sum(list_num) / len(list_num))

# # Vowel Counter
# sentence = input("Enter an sentence : ").lower().strip()
# vowels = "aeiou"
# count_constants = 0
# count_vowels = 0

# for sen in sentence:
#     if sen.isalpha():
#         if sen in vowels:
#             count_vowels += 1
#         else:
#             count_constants += 1

# print(count_vowels)
# print(count_constants)

# # Multiplication Table Generator
# num = int(input("Enter the number u want the table of : "))
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# # Reverse a String (Using a Loop)
# word = str(input("Enter an word : ")).lower().strip()

# reverse_word = ""
# for char in word:
#     reverse_word = char + reverse_word

# print(reverse_word)

# Exercise 5 — Menu Loop
while True:
    print("1. Say Hello")
    print("2. Show your name")
    print("3. Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        print("Hello!\n\n")
    elif choice == 2:
        name = str(input("Enter your name : ")).strip().title()
        print(name, "\n\n")
    else:
        break
