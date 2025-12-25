amount_of_expense = int(input("Enter number of expenses : "))

expense_tracker = {}
for amount in range(amount_of_expense):
    category = input("Enter category : ").strip()
    expense_amount = int(input("Enter amount : "))
    if category in expense_tracker:
        expense_tracker[category] += expense_amount
    else:
        expense_tracker[category] = expense_amount

print("Expense Summary:")
for keys in expense_tracker:
    print(f"{keys} : {expense_tracker[keys]}")

total = 0
for k in expense_tracker.values():
    total += k

print(f"\nTotal Expense : {total}")

highest_expence_count = 0
highest_expence_category = ""

for exp in expense_tracker:
    if expense_tracker[exp] > highest_expence_count:
        highest_expence_count = expense_tracker[exp]
        highest_expence_category = exp

print(f"highest_expence_category : {highest_expence_category}")
