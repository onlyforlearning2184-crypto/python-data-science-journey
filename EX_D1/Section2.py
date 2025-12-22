User = int(input("Enter the number : "))
# u can use User = int(User) if u dont want to use constructure directly
if User > 0:
    print("Positive")
elif User < 0:
    print("Negative")
else:
    print("Zero")


num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))


print("Sum : ", num1 + num2)
print("Difference : ", num1 - num2)
print("Product : ", num1 * num2)
if num2 != 0:
    print("Quotient : ", round(num1 / num2, 2))
else:
    print("division by zero is not posible")

new_num = int(input("Enter the number : "))
# u can use /(divide) or % (modulos)
if new_num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

Age = int(input("Enter your Age : "))
if Age < 13 and Age > 0:
    print("Child")

elif Age >= 13 and Age <= 19:
    print("Teen")

elif Age >= 20 and Age <= 59:
    print("Adult")

elif Age >= 60:
    print("Senior")

else:
    print("invalid input")


# Grade evaluator
new_num = int(input("Enter the score"))
if new_num == 100:  # just for fun
    print("Perfect score, Bravo!👍👍")
elif new_num >= 90 and new_num <= 99:
    print("A")
elif new_num >= 80 and new_num <= 89:
    print("B")
elif new_num >= 70 and new_num <= 79:
    print("C")
elif new_num >= 60 and new_num <= 69:
    print("D")
else:
    print("F")


c = float(input("Enter the temperature in celsius : "))
f = (c * 9 / 5) + 32

print(c, " in fahrenheit is ", f)

a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
c = int(input("Enter the number : "))

# if a > b and a > c:
#     print(a, " is largest")

# elif b > c and b > a:
#     print(b, " is largest")

# elif c > a and c > b:
#     print(c, " is largest")

# else:
#     print("All are equal")

if a == b == c:
    print("All are equal")
elif a >= b and a >= c:
    print(a, "is largest")
elif b >= a and b >= c:
    print(b, "is largest")
else:
    print(c, "is largest")


# Mini task
import math as m

num = int(input("Enter the number : "))

print(abs(num))
print(round(num))
print(round(num, 1))
if num >= 0:
    print(m.sqrt(num))
else:
    print("Square root not defined for negative numbers")
print(m.ceil(num))
print(m.floor(num))
