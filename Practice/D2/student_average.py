students = {"Tirth": [100, 80, 90, 85], "Krupa": [80, 90, 70, 60]}

for student in students:
    total = sum(students[student])
    avg = total / len(students[student])

    print(student, ":", round(avg, 2))
