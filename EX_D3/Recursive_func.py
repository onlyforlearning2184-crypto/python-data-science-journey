# # Exercise 11 — Recursive Countdown
# def countdown(n):
#     print(n)
#     n -= 1
#     if n == 0:
#         return
#     countdown(n)


# countdown(5)


# # Exercise 12 — Recursive Sum
# def sum_n(n):
#     if n == 1:
#         return 1
#     return n + sum_n(n - 1)


# print(sum_n(15))

# Exercise 13 — Recursive Factorial


def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
