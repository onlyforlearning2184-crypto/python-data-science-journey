try:
    with open("logs.txt", "r") as f:
        text_line = f.read().splitlines()
        counts = {}

        for line in text_line:
            parts = line.split(" ")
            f_part = parts[0]
            if f_part not in counts:
                counts[f_part] = 1
            else:
                counts[f_part] += 1

        print("Log Counts: ")
        for key in counts:
            print(f"{key} : {counts[key]}")

except FileNotFoundError:
    print("File not fdound")
