u_name = input("Enter the name : ").strip()
u_age = int(input("Enter the age : ").strip())
u_city = input("Enter the city : ").strip()

student = {"name": u_name, "age": u_age, "city": u_city}
print(student)

tup = tuple(student.values())
print(tup)
