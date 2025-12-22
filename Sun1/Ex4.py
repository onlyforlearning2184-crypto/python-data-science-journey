items = ("Coffee", "Tea", "Sandwich", "Juice")
prices = (2, 1, 5, 3)
menu = [items, prices]

user = input("Enter the item you want : ").strip().title()
if user == items[1]:
    print(user, " : $", prices[1])
elif user == items[0]:
    print(user, " : $", prices[0])
elif user == items[2]:
    print(user, " : $", prices[2])
elif user == items[3]:
    print(user, " : $", prices[3])
else:
    print("Not in menu")
