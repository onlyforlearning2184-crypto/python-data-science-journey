people = [
    {"name": "A", "age": 20, "colors": ("red", "blue")},
    {"name": "B", "age": 25, "colors": ("green", "yellow")},
    {"name": "C", "age": 30, "colors": ("black", "white")},
]
print(people[0]["colors"])
print(people[-1]["age"])

unique_colors = set()

unique_colors.update(people[0]["colors"])
unique_colors.update(people[1]["colors"])
unique_colors.update(people[2]["colors"])

print(unique_colors)
