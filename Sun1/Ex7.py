emp1 = {"name": "John", "age": 30}
emp2 = {"name": "Sarah", "age": 28}
company = {"e1": emp1, "e2": emp2}

names = tuple((company["e1"]["name"], company["e2"]["name"]))
print(names)
