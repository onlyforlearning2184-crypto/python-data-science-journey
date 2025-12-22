def sum_of_digits(n):
    total = 0

    while n > 0:
        last_digit = n % 10
        total += last_digit
        n = n // 10

    return total


print(sum_of_digits(123))


def recursive_sum_of_digits(n):
    if n == 0:
        return 0
    last_num = n % 10
    rest_num = n // 10

    return last_num + recursive_sum_of_digits(rest_num)


print(recursive_sum_of_digits(1234))
