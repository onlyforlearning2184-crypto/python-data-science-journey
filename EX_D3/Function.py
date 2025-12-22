# # Greeting Function
# def greet(name):
#     print("Hello", name)


# u_name = str(input("Enter your name : ")).strip().title()
# greet(u_name)


# # Exercise 7 — Simple Calculator (Using Functions)
# def add(a, b):
#     return a + b


# def sub(a, b):
#     return a - b


# def mul(a, b):
#     return a * b


# def div(a, b):
#     return a / b


# num1 = int(input("Enter the number 1 : \n"))
# num2 = int(input("Enter the number 2 : \n"))
# print("Operations : +, -, *, /")
# operation = input("Enter the operation from u want to perform : ")

# if operation == "+":
#     print(add(num1, num2))

# elif operation == "-":
#     print(sub(num1, num2))

# elif operation == "*":
#     print(mul(num1, num2))

# elif operation == "/":
#     if num2 == 0:
#         print("Can not divede by zero")
#     else:
#         print(div(num1, num2))


# # Exercise 8 — Even / Odd Checker (Function)
# def check(num):
#     if num % 2 == 0:
#         print("The number is Even")
#     else:
#         print("The number is Odd")


# number = int(input("Enter an number : "))
# check(number)


# # Exercise 9 — List Filter Function
# def get_even(numbers):
#     ev = []
#     for n in numbers:
#         if n % 2 == 0:
#             ev.append(n)
#     return ev


# nums = []
# for i in range(5):
#     num = int(input("Enter number : "))
#     nums.append(num)

# result = get_even(nums)

# print("Even numbers:", result)

# # Exercise 10 — Login System (Functions + Loops)
# def login(user, password):
#     correct_user = "admin"
#     correct_pass = "1234"
#     if user == correct_user and password == correct_pass:
#         return True
#     else:
#         return False


# for i in range(0, 3):
#     user = str(input("Enter the username : ")).strip().lower()
#     password = str(input("Enter the password : ")).strip().lower()
#     attempts = i + 1
#     print("Attempt : ", attempts)

#     if login(user, password):
#         print("Login successful!")
#         break
# else:
#   print("Access denied!")
