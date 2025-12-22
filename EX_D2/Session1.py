# Tuple basics
tup = ("red", "yellow", "black", "green")
print(tup[0])
print(tup[-1])
print(len(tup))


# Tuple packing & unpacking
data = ("John", 25, "London")
(name, age, city) = data
print(name)
print(age)
print(city)

# Modify tuple indirectly
colors = ("red", "blue", "green")
li = list(colors)
li.append("yellow")

new_colors = tuple((li))
print(new_colors)

# Tuple Slicing

nums = (2, 4, 6, 8, 10, 12)

print(nums[0:3])
print(nums[-2:])
print(nums[0::2])

# Star Unpacking
items = (1, 2, 3, 4, 5, 6)

(a, *b, c) = items
print(a)
print(b)
print(c)
