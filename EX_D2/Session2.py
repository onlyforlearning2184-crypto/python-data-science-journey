# Basic Dictionary
person = {"name": "Alice", "age": 20, "city": "Paris"}
print(person["name"])
print(person.keys())
print(person.values())

# Add & Update

student = {"name": "Bob", "grade": "B"}
student["grade"] = "A"
student["age"] = 18
print(student)

# Remove items
car = {"brand": "Toyota", "year": 2019, "color": "Black"}
car.pop("color")
car["model"] = "corolla"
print(car)

# Nested Dictionary
players = {"p1": {"name": "Leo", "score": 90}, "p2": {"name": "Mia", "score": 85}}

print(players["p1"]["name"])
print(players["p2"]["score"])

# Dictionary Copy Practice
d1 = {"x": 10, "y": 20}

d2 = d1

d3 = d1.copy()
d1["x"] = 99

print(d1)
print(d2)
print(d3)
