li = ["apple", "banana", "apple"]
count_li = {}

for items in li:
    if items in count_li:
        count_li[items] += 1
    else:
        count_li[items] = 1

print(count_li)
