name = input("Enter your name : ")
print("Hello ", name, "! Welcome to Python!")

Fav_color = input("Enter your favorite color : ")
Fav_food = input("Enter your favorite food : ")
Fav_hobby = input("Enter your favorite hobby : ")

print(
    "Your favorite color is ",
    Fav_color,
    ", you love",
    Fav_food,
    ", and you enjoy",
    Fav_hobby,
    ".",
)

year_Op = input("Enter your favorite year : ")
sen = "I love to eat PIZZA during the YEAR."

sen = sen.replace("PIZZA", Fav_food)
sen = sen.replace("YEAR", year_Op)
print(sen)

Full_name = input("Enter your full name in Random case : ")
Full_name = Full_name.strip().title()
print("Your clean name : ", Full_name)

User = input("Enter any word : ")
User = User.upper()  # or print(User.upper())
print(User)
User = User.lower()  # or print(User.lower())
print(User)
User = User.title()  # or print(User.title())
print(User)
