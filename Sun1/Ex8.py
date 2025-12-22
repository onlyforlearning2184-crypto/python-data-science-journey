account = {"name": "Alice", "balance": 1000}
user = input("Enter d for deposit and w for withdrawal : ").strip().lower()
if user == "d":
    deposit_amount = int(input("Enter the deposit amount : "))
    account["balance"] += deposit_amount
    print("Your total balance is : ", account["balance"])


elif user == "w":
    withdrawal_amount = int(input("Enter the withdrawal amount : "))
    account["balance"] -= withdrawal_amount
    print("Your total balance after withdrawal is : ", account["balance"])

else:
    print("Invalid choice")
