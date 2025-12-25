try:
    with open("sales.txt", "r") as f:
        line_wise_sales = f.read().splitlines()
        sales_dict = {}
        total = 0
        for sale in line_wise_sales:
            part = sale.split(",")
            product = part[0]
            amount = int(part[1])
            if product in sales_dict:
                sales_dict[product] += amount
            else:
                sales_dict[product] = amount

            total += amount

        print(f"Total Sales : {total}")
        print("Product-wise Sales : ")
        for key in sales_dict:
            print(f"{key} : {sales_dict[key]}")

except FileNotFoundError:
    print("File not found")
