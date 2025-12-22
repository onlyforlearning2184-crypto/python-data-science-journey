# string data type

# literal assignment
first = "Tirth"
last = "Prajapati"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Cunstructor function
pizza = str("Pepperoni")  # str is cunstructor function
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation

fullname = first + " " + last
# print(fullname)
fullname += "!"

# castinng a number to a string also called type_casting
decade = str(1980)
# print(type(decade))
# print(decade)

statement = "I like music from the " + decade + "s."
# print(statement)

# multiple Line
multiline = """
Hey, how are you

I was just checking in.
                                All good?

"""
# print(multiline)

# escaping special characters
sentence = "I'm back at work!\tHey!\n\nWhere's this at\\located?"
# print(sentence)

# String Methods

# print(first)
# print(first.lower())
# print(first.upper())

# print(multiline.title())  # Change the 1st letter of the word to uppercase
# print(multiline.replace("good", "ok"))  # Change the good with ok and does not modify the original

# print(len(multiline))
multiline += "                                                                                                           "
multiline = "                                            " + multiline
# print(len(multiline))

# print(len(multiline.strip()))  # remove withspaces
# print(len(multiline.lstrip()))  # remove withspaces
# print(len(multiline.rstrip()))  # remove withspaces

# Build a menu
title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + "$1".rjust(4))  # left justify and right justify
# print("Tea".ljust(16, ".") + "$0.5".rjust(4))  # left justify and right justify
# print("Choclate Cake".ljust(16, ".") + "$6".rjust(4))  # left justify and right justify

# String index values
# print(first[0])
# print(first[1])
# print(first[2])
# print(first[3])
# print(first[4])
# print("")
# print(first[0])
# print(first[-4])
# print(first[-3])
# print(first[-2])
# print(first[-1])
# print("")
# print(first[0:5])
# print(first[-5:])
# print(first[-5 : len(first)])
# print(first[::])

# some methods return boolean data
# print(first.startswith("T"))
# print(first.endswith("Z"))
# print(first.startswith("t"))

# boolean data type
myvalue = True
x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))

# numeric Data Type

# integer type
pric = 100
best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))

# Float type
gpa = 3.28
y = float(gpa)
# print(type(gpa))
# print(isinstance(y, float))

# complex type
comp_value = 5 + 3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting string to number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zipcode))
print(type(zip_value))

# Error if u try to cast incorrect data
# zip_value = int("new york")
