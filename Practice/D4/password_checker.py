password = input("Enter the password : ").strip()


resons = []
if len(password) < 8:
    resons.append("Less than 8 characters")

has_upper = False
has_lower = False
has_digit = False
for char in password:

    if char.islower():
        has_lower = True

    if char.isupper():
        has_upper = True

    if char.isdigit():
        has_digit = True

if not has_upper:
    resons.append("Does not contain any uppercase letter!")

if not has_lower:
    resons.append("Does not contain any lowercase letter!")

if not has_digit:
    resons.append("Does not contain any digits!")

if len(resons) == 0:
    print("Strong password")

else:
    print("Weak password")
    for reson in resons:
        print(f"- {reson}")
