contact = {"name": "", "email": "", "phone": ""}
u_name = input("Enter the name : ").strip().lower()
u_email = input("Enter the email : ").strip().lower()
u_phone = input("Enter the phone : ").strip()

contact["name"] = u_name
contact["email"] = u_email
contact["phone"] = u_phone

contacts = [contact]
print(contacts)
