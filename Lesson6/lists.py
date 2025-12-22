users = ["Dave", "John", "Sara"]
data = ["Dave", 42, True]

empty_Lists = []

print("Dave" in empty_Lists)

print(users[0])
print(users[-2])

print(users.index("Sara"))  # list method

print(users[0:2])  # slicing
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Elsa")  # Adding
# print(users)

users += ["Jason"]  # without [] it will add the characters individualy
# print(users)
users.extend(["Robert", "Jimmy"])
# print(users)

# users.extend(data)
# print(users)
users.insert(0, "Bob")
# print(users)

users[2:2] = ["Eddie", "Alex"]  # Bracket notation
# print(users)

users[1:3] = ["Robert", "JPJ"]
# print(users)
# print(users)

users.remove("Bob")  # Removing
# print(users)

# print(users.pop())  # pop Method
# print(users)

del users[0]
# print(users)

# del data
data.clear()
# print(data)

users[1:2] = ["dave"]
users.sort()
# print(users)

users.sort(key=str.lower)
# print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
# print(nums)

nums.sort(reverse=True)  # descending
# print(nums)
nums.sort(reverse=False)  # ascending
# print(nums)

print(
    sorted(nums, reverse=True)
)  # Another way fors sorting Using Globle Shorted function Does not modify the original

nums_copy = nums.copy()
my_nums = list(nums)
my_copy = nums[:]
# print(nums_copy)
# print(my_nums)
my_copy.sort(reverse=True)
# print(my_copy)
# print(nums)

print(type(nums))
