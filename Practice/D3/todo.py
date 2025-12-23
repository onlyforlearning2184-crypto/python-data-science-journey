# def add_task():
#     task = input("Enter task: ")
#     with open("tasks.txt", "a") as f:
#         f.write(task + "\n")


# def view_tasks():
#     try:
#         with open("tasks.txt", "r") as f:
#             tasks = f.read().splitlines()

#         if not tasks:
#             print("No tasks found.")
#             return

#         for i, task in enumerate(tasks, start=1):
#             print(f"{i}. {task}")

#     except FileNotFoundError:
#         print("No tasks found.")


# while True:
#     print("\n1. Add task\n2. View tasks\n3. Exit")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_task()
#     elif choice == "2":
#         view_tasks()
#     elif choice == "3":
#         print("Exiting To-Do App...")
#         break
#     else:
#         print("Invalid choice, try again")

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        with open("tasks.txt", "a") as f:
            f.write(task + "\n")
        print("Task added.")

    elif choice == "2":
        with open("tasks.txt", "a+") as f:
            f.seek(0)
            tasks = f.read().splitlines()

        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")
