# # guest list builder
# name = []  # empty list
# name_1 = input("Enter name 1 : ").strip().title()
# name_2 = input("Enter name 2 : ").strip().title()
# name_3 = input("Enter name 3 : ").strip().title()
# name_4 = input("Enter name 4 : ").strip().title()
# name_5 = input("Enter name 5 : ").strip().title()

# name.append(name_1)
# name.append(name_2)
# name.append(name_3)
# name.append(name_4)
# name.append(name_5)

# print("Final list : ", name)

# # List Editor

# users = ["Dave", "John", "Sara"]
# print(users)
# users.insert(0, "Bob")
# print(users)
# users[2] = "Robert"
# print(users)
# users.extend(["Emily", "Chirs"])
# print(users)
# users.remove("Sara")
# print(users)

# First & last items
# Sep_User = input("Enter the list items : ")
# list_sep = list(Sep_User.strip().split(","))
# print(list_sep)
# print(list_sep[0])
# print(list_sep[-1])

# Number sorting
# number = []  # empty list
# number_1 = int(input("Enter number 1 : "))
# number_2 = int(input("Enter number 2 : "))
# number_3 = int(input("Enter number 3 : "))
# number_4 = int(input("Enter number 4 : "))
# number_5 = int(input("Enter number 5 : "))

# number.append(number_1)
# number.append(number_2)
# number.append(number_3)
# number.append(number_4)
# number.append(number_5)

# print(number)
# number.sort()
# print(number)
# number.sort(reverse=True)
# print(number)
# print(sorted(number))

# Remove Duplicates

# nums = [2, 4, 2, 6, 4, 8, 6, 8]
# print(nums)
# new_nums = []

# if nums[0] not in new_nums:
#     new_nums.append(nums[0])
# if nums[1] not in new_nums:
#     new_nums.append(nums[1])
# if nums[2] not in new_nums:
#     new_nums.append(nums[2])
# if nums[3] not in new_nums:
#     new_nums.append(nums[3])
# if nums[4] not in new_nums:
#     new_nums.append(nums[4])
# if nums[5] not in new_nums:
#     new_nums.append(nums[5])
# if nums[6] not in new_nums:
#     new_nums.append(nums[6])
# if nums[7] not in new_nums:
#     new_nums.append(nums[7])

# print(new_nums)


# # Shopping list manager
# import sys

# shopping = []

# add_item = input("Add an item : ")
# shopping.append(add_item)

# annother = input("If you want to add another item then say yes :").title().strip()
# if annother == "yes".title():
#     another_item = input("Add an item : ")
#     shopping.append(another_item)

# else:
#     sys.exit

# remove = input("If you want to remove an item say yes: ").title().strip()
# if remove == "yes".title():
#     remove_item = input("Remove an item : ")
#     shopping.remove(remove_item)

# else:
#     sys.exit

# print(shopping)


# # Slice printer
# animals = ["cat", "dog", "cow", "lion", "tiger", "zebra"]

# print(animals[0:3])
# print(animals[-2:])
# print(animals[0::2])
# animals.reverse()  # or use print(animals[::-1])
# print(animals)


# # Search Item
# fruits = ["apple", "banana", "mango", "orange", "grape"]

# fr_user = input("Enter a fruit").lower().strip()
# if fr_user in fruits:
#     print("Found")

# else:
#     print("Not found")

# # Pair Lists
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]

# print(names[0], " : ", scores[0])
# print(names[1], " : ", scores[1])
# print(names[2], " : ", scores[2])
