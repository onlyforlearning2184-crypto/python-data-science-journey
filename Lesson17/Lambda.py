# def squared(num):
#     return num * num


# print(squared(2))


# squred = lambda num1: num1 + num1  # noqa: E731
# print(squred(2))


# # def sum(a, b):
# #     return a + b


# sum = lambda a, b: a + b  # noqa: E731
# print(sum(10, 2))

# ####################################################################
# # Use as quick function


# def func_builder(x):
#     return lambda num: num * x


# mul10 = func_builder(10)
# mul20 = func_builder(20)

# print(mul10(2))
# print(mul20(3))

############################################

nums = [10, 2, 43, 5, 12, 67, 8, 11]

squared_nums = map(lambda num: num * num, nums)

print(list(squared_nums))

############################################

fillterd_nums = filter(lambda num: num % 2 != 0, nums)
print(list(fillterd_nums))

############################################

from functools import reduce  # noqa: E402


numbers = [1, 2, 3, 4, 5, 1, 5]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)

print(sum(numbers, 10))

names = ["tirth", "rachit", "krupa", "asa", "krisha", "disha", "sweeta"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)
