try:
    with open("data.txt", "r") as f:
        data_lines = f.read().splitlines()
        summary_repost = {}
        total = 0
        for lines in data_lines:
            parts = lines.split(",")

            category = parts[0]
            amount = int(parts[1])

            total += amount

            if category not in summary_repost:
                summary_repost[category] = amount
            else:
                summary_repost[category] += amount

        with open("report.txt", "w") as nf:
            nf.write("SUMMARY REPORT\n")
            nf.write("--------------------- \n")
            nf.write(f"Total Amount : {total}\n")
            nf.write("Category-wise Totals\n")
            for key in summary_repost:
                nf.write(f"{key} : {summary_repost[key]}\n")


except FileNotFoundError:
    print("File not found!")
