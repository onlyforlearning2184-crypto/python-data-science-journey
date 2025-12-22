# # Print this exact pattern:
# # *
# # **
# # ***
# # ****

# for i in range(0, 5):
#     print("*" * i)

# # 2️⃣ Take a string from the user and:
# string = str(input("Enter the string : "))
# new_string = string.replace(" ", "")
# print(new_string)

# titled_Case = string.title()
# print(titled_Case)

# new_sr = ""
# vovels = "aeiouAEIOU"
# for char in string:
#     if char in vovels:
#         New_sr += "*"
#     else:
#         New_sr += char

# print(New_sr)


# # 3️⃣ Check if a number is odd, even, or zero

# num = int(input("Enter the nukber : "))
# if num == 0:
#     print("Number is Zero")

# elif num % 2 == 0:  # or num/2==0
#     print("Number is Even")

# else:
#     print("Number is Odd")


# # 4️⃣ Get 3 numbers and print the LARGEST and SMALLEST (without max() or min())

# a, b, c = 10, 20, 30

# if a > b and a > c:
#     print(f"Largest is {a}.")
# elif b > a and b > c:
#     print(f"Largest is {b}.")
# elif c > a and c > b:
#     print(f"Largest is {c}.")


# if a < b and a < c:
#     print(f"Smallest is {a}.")
# elif b < a and b < c:
#     print(f"Smallest is {b}.")
# elif c < b and c < a:
#     print(f"Smallest is {c}.")

# # 5️⃣ Count how many times each character appears in a string (frequency counter)
# string = str(input("Enter a string : ")).strip()

# new_string = {}

# for char in string:
#     if char in new_string:
#         new_string[char] += 1
#     else:
#         new_string[char] = 1

# for key in new_string:
#     print(key, new_string[key])

# # 6️⃣ Remove duplicates from a list WITHOUT using set()

# numbers = [1, 2, 2, 3, 3, 3, 4, 1, 2]
# num = []
# for numbs in numbers:
#     if numbs not in num:
#         num.append(numbs)
# print(num)


# # 7️⃣ Tuple Slicing Practice

# t = (10, 20, 30, 40, 50)

# print(t[0:2])
# print(t[-2:])

# print(t[2])

# print(t[::-1])
# # ex = list(t)
# # ex.sort(reverse=True)
# # new_t = tuple(ex)

# # print(new_t)


# # 8️⃣ Convert this dictionary into two lists
# dic = {"name": "tirth", "age": 18, "course": "python"}
# li1 = list(dic.keys())
# li2 = list(dic.values())

# print(li1)
# print(li2)

# # 9️⃣ Count how many times each character appears (but skip spaces)
# string = str(input("Enter a string : ")).strip()

# new_string = {}

# for char in string:
#     if char in new_string:
#         new_string[char] += 1
#     elif char == " ":
#         continue
#     else:
#         new_string[char] = 1

# for key in new_string:
#     print(key, new_string[key])


# # 🔟 Print a multiplication table (1–20)

# num = int(input("Enter the number : "))

# for i in range(1, 21):
#     print(f"{num} X {i} = {num*i}")

# # 1️⃣ Create a Menu Loop

# items = []

# while True:
#     print("---------Shooping Cart---------")
#     print("1. Add item")
#     print("2. Remove item")
#     print("3. view items")
#     print("4. Exit\n\n")

#     choice = int(input("Enter your choice : "))

#     if choice == 1:
#         add_item = str(input("\\nEnter the item you want to add : ")).strip().title()
#         items.append(add_item)
#         print(f"\n{add_item} added in the cart.")

#     elif choice == 2:
#         remove_item = (
#             str(input("\\nEnter the item you want to remove : ")).strip().title()
#         )
#         if remove_item not in items:
#             print(f"You dont have {remove_item} in you list")
#         else:
#             items.remove(remove_item)
#             print(f"\n{remove_item} removed from the cart.")

#     elif choice == 3:
#         count = 0
#         if len(items) == 0:
#             print("\nYour cart is empty\n")
#         else:
#             for i in items:
#                 count += 1
#                 print(f"Item_{count} : {i}")
#     elif choice == 4:
#           print("Thanks for using the shopping cart!")
#           break
#     else:
#         print("Invalid input, Choose from 1,2,3 and 4 ")

# # 2️⃣ Reverse a string manually (no slicing allowed)
# string = str(input("Enter the string : ")).strip()
# new_string = ""
# for char in string:
#     new_string = char + new_string

# print(new_string)


# # Write a function that returns the 2nd largest number in a list
# def second_largest(nums):
#     largest = nums[0]
#     for i in nums:
#         if largest < i:
#             largest = i

#     second_largest = None
#     for sec in nums:
#         if sec != largest:
#             if second_largest is None or sec > second_largest:
#                 second_largest = sec

#     return second_largest


# second_largest([10, 20, 4, 7])


# # 4️⃣ Write a function that checks if a string is a palindrome
# def is_palindrome(text):
#     text = text.lower()
#     rev_text = ""
#     for char in text:
#         rev_text = char + rev_text
#     if text == rev_text:
#         return True
#     else:
#         return False


# print(is_palindrome("anana"))


# # 5️⃣ Write a function that returns only even numbers from a list
# def get_evens(numbers):
#     new_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             new_numbers.append(num)

#     return new_numbers


# print(get_evens([1, 2, 3, 4, 5, 6]))


# # 6️⃣ Build a Mini Calculator using Functions


# def add(a, b):
#     return a + b


# def subtract(a, b):
#     return a - b


# def multiply(a, b):
#     return a * b


# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError
#     return a / b


# print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")
# choice = int(input("Enter your choice : "))
# if choice not in [1, 2, 3, 4]:
#     print("Invalid input try again")

# a = int(input("Enter the number : "))
# b = int(input("Enter the number : "))

# if choice == 1:
#     print(f"a + b = {add(a,b)}")

# elif choice == 2:
#     print(f"a - b = {subtract(a,b)}")

# elif choice == 3:
#     print(f"a * b = {multiply(a,b)}")

# else:
#     print(f"a / b = {divide(a,b)}")


# # 7️⃣ Recursive Factorial

# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)


# fac = factorial(6)
# print(fac)


# # 8️⃣ Recursive Fibonacci
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


# print(fib(6))

# # 9️⃣ Recursive Reverse String


# def rev_string(string):
#     if len(string) == 0 or len(string) == 1:
#         return string
#     first_char = string[0]
#     rest = string[1:]
#     return rev_string(rest) + first_char


# print(rev_string("banana"))


# # 0️⃣ Recursive Sum of Digits
# def sum_digits(n):
#     if n == 0:
#         return 0

#     last_digits = n % 10
#     rest_digits = n // 10

#     return last_digits + sum_digits(rest_digits)


# print(sum_digits(1234))
