# username Generator
f_name = str(input("Enter your first name : "))
l_name = str(input("Enter your last name : "))

user_name = (f_name[0:3] + l_name[-3:]).lower()
print(user_name)

# Menu formatter

print("MENU".center(20, "="))
print("Coffee".ljust(16, ".") + "$2".rjust(4))
print("Tea".ljust(16, ".") + "$1".rjust(4))
print("Sandwich".ljust(16, ".") + "$5".rjust(4))


# Word Analyzer
word = input("Enter a word: ").strip()

print("Length:", len(word))
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Uppercase:", word.upper())

if word.lower().startswith("a"):  # or if word[0].lower() == 'a'
    print("It starts with 'a'")
else:
    print("Does not start with 'a'")
