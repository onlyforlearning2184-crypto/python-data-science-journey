# person = "Rachit"
# coins = 3

# print("\n" + person + " has " + str(coins) + " coins left.")

# message = "\n%s has %s coins left." % (person, coins)
# print(message)

# message1 = "\n{} has {} coins left.".format(person, coins)
# print(message1)

# message3 = "\n{1} has {0} coins left.".format(coins, person)  # index
# print(message)

# message4 = "\n{person} has {coins} coins left.".format(coins=coins, person=person)
# print(message)


# message_best = f"\n{person} has {coins} coins left."
# print(message_best)

# message_best2 = f"\n{person.lower()} has {coins * 2} coins left."
# print(message_best)

##########
# you can pass formmating optins

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is  {num / 4.25:.2%}")
