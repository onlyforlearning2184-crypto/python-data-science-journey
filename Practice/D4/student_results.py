def add_student():
    name = input("Enter the student the name : ").strip().title()
    amount_marks = int(input("Enter the number of subject : "))
    with open("student_report.txt", "a") as f:
        f.write(f"{name}")
        for i in range(amount_marks):
            marks = int(input(f"Enter the marks of the subject{i} : "))
            with open("student_report.txt", "a") as f:
                f.write(f",{marks}")
        f.write("\n")


def view_result():
    try:
        with open("student_report.txt", "r") as f:
            report = f.read().splitlines()
        for i in report:
            parts = i.split(",")
            name_part = parts[0]

            marks = []
            for mark in parts[1:]:
                marks.append(int(mark))

            total = 0
            for ma in marks:
                total += ma

            avg_part = total / len(marks)

            print(f"Student Name : {name_part}")
            print(f"Marks : {marks}")
            print(f"Average Marks : {avg_part}\n\n")
    except FileNotFoundError:
        print("No student_result found!")


while True:
    print("\n1. Add student\n2. View result\n3. Exit\n")
    choice = input("Enter your choice : ").strip()

    if choice not in "123":
        print("Invalid choice, try again!")
    else:
        if choice == "1":
            add_student()
        elif choice == "2":
            view_result()
        elif choice == "3":
            break
