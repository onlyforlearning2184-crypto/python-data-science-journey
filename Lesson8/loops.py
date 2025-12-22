# While looops
# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1
# value = 1
# while value <= 10:
#     value += 1
#     print(value)

#     if value == 5:
#         continue

# else:
#     print(value)
# names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# for x in "america is shit":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)


# for x in range(4):  # Start, Stop, Steps
#     print(x)

# for x in range(2, 4):
#     print(x)

# for x in range(5, 101, 5):
#     print(x)
# else:
#     print("Glad thats's over")

names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name, ":", action)

for action in actions:
    for name in names:
        print(name, ":", action)
