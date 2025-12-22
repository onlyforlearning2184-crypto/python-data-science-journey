def hello():
    print("hello")


hello()


# def sum(num1, num2):
def sum(num1=4, num2=5):

    # print(num1 + num2)
    if type(num1) is not int or type(num2) is not int:
        # return "Its not a number!"
        return 0
    return num1 + num2


# sum(2, 3)
# sum(7, 3)
# sum(2, 8)
# total = sum(2, 5)
# total = sum(2, "s")
total = sum()
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")


def multi_names(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_names(first="Dave", last="Gray")
