try:
    with open("students.txt", "r") as f:
        students = f.read().splitlines()
        # student_result = {}
        student_result = []

        for student in students:
            parts = student.split(",")
            student_part = parts[0]
            marks_part = parts[1:]
            total_marks = 0
            for i in marks_part:
                total_marks = int(i) + total_marks
            avg = total_marks / len(marks_part)
            # if student_part not in student_result:
            #     student_result[student_part] = round(avg, 2)
            # else:
            #     student_result[student_part] += avg
            student_result.append((student_part, round(avg, 2)))

        student_result.sort(key=lambda x: x[1], reverse=True)
        print("Rank List:")
        rank = 1
        for student_part, avg in student_result:
            print(f"{rank}. {student_part} - {avg}")
            rank += 1

except FileNotFoundError:
    print("File not found!")
