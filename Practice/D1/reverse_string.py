def reverse_string(string):
    rev_string = ""
    for char in string:
        rev_string = char + rev_string

    return rev_string


print(reverse_string("banana"))


def recursive_rev_string(string):
    if len(string) <= 1:
        return string

    first_char = string[0]
    rest_char = string[1:]

    return recursive_rev_string(rest_char) + first_char


print(recursive_rev_string("kaju"))
