n1 = int(input("Enter the number1 : "))
n2 = int(input("Enter the number2 : "))
n3 = int(input("Enter the number3 : "))

if n1==n2==n3:
    print("All are Equal")

elif n1>n2 and n1>n3:
    print(f"{n1} is largest.")

elif n2>n1 and n2>n3:
    print(f"{n2} is largest.")

elif n3>n2 and n3>n1:
    print(f"{n3} is largest.")
