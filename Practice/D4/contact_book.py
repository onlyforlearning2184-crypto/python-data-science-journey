def add_contact():
    name = input("Enter the  the name : ").strip().title()
    phone_number = input("Enter the phone number : ").strip()
    with open("contacts.txt", "a") as f:
        f.write(f"{name},{phone_number}\n")
    print("Contact saved successfully\n")


def view_contacts():
    try:
        with open("contacts.txt", "r") as f:
            contact = f.read().splitlines()

        print("Contacts: ")
        print("-" * 30)

        for i in contact:
            parts = i.split(",")
            name_part = parts[0]
            number_part = parts[1]
            print(f"{name_part} - {number_part}")

    except FileNotFoundError:
        print("\nNo contacts named file found!\n")


def search_contact():
    try:
        search = input("Enter name to search : ").strip().title()
        with open("contacts.txt", "r") as f:
            contact_search = f.read().splitlines()

        if search in contact_search:
            print("Contact found:")
            for i in contact_search:
                parts = i.split(",")
                name_part = parts[0]
                num_part = parts[1]
                if search == name_part:
                    print(f"{name_part} : {num_part}")

        else:
            print("Contact not found")

    except FileNotFoundError:
        print("\nNo contacts named file found!\n")


while True:
    print("\n1. Add contact\n2. View contacts\n3. Search contact\n4. Exit\n")
    choice = input("Enter your choice : ").strip()

    if choice not in "1234":
        print("Invalid choice, try again!")
    else:
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            break
