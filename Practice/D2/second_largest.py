li = [10, 5, 8, 20, 15]

larg_num = li[0]
sec_large_num = li[0]
for n in li:
    if n > larg_num:
        sec_large_num = larg_num
        larg_num = n
    elif n != larg_num and sec_large_num < n:
        sec_large_num = n
print(sec_large_num)
