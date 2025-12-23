num = [1, 2, 2, 3, 1, 4]
new_list = []

for n in num:
    if n not in new_list:
        new_list.append(n)

print(new_list)
