fruits = ["apple", "banana", "apple", "mango", "banana"]
set_fruits = set(fruits)

new_fruits = sorted(set_fruits)
print(new_fruits)

fruits_name = input("Enter the fruit name : ").strip().lower()
if fruits_name in new_fruits:
    print("Available")
else:
    print("Not available")
