try:
    with open("expenses.txt", "r") as f:
        line_wise_months = f.read().splitlines()

        data = {}
        total_amount = {}

        for month in line_wise_months:
            parts = month.split(",")
            month = parts[0]
            if month not in data:
                data[month] = {}

            category = parts[1]
            amount = int(parts[2])
            if category in data[month]:
                data[month][category] += amount
            else:
                data[month][category] = amount

            if month not in total_amount:
                total_amount[month] = amount
            else:
                total_amount[month] += amount

        print("Monthly Totals: ")
        for month in total_amount:
            print(f"{month} : {total_amount[month]}")

        print("\nCategory-wise Monthly Totals:")
        for month in data:
            print(month)
            for category in data[month]:
                print(" ", category, ":", data[month][category])


except FileNotFoundError:
    print("File not found")
