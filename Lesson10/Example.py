value = True
count = 0
while value:
    count += 1
    print(count)
    # value = 0  # 0 = false and 1 is true
    if count == 5:
        break
    else:
        value = 0
        continue
