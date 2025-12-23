def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n")
    choice = int(input("Enter your choice : "))

    if choice not in [1, 2, 3, 4, 5]:
        print("Invalid input try again")

    if choice == "5":
        print("Exiting calculator...")
        break

    a = int(input("Enter the number : "))
    b = int(input("Enter the number : "))

    if choice == 1:
        print(f"a + b = {add(a,b)}")

    elif choice == 2:
        print(f"a - b = {subtract(a,b)}")

    elif choice == 3:
        print(f"a * b = {multiply(a,b)}")

    elif choice == 4:
        print(f"a / b = {divide(a,b)}")
