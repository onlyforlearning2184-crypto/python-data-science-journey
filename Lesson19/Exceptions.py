class Just_Not_Cool_Error(Exception):
    pass


x = 1
try:
    raise Just_Not_Cool_Error("This just isn't cool, man.")
    # raise Exception("I'm a custom Exception!")

    # print(x)
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only string are allowed.")
except NameError:  # run when cought error
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("Please do not divide by zero.")
except Exception as error:
    print(error)
else:  # run if there's no error
    print("No errors!")
finally:  # run even if there's error or no error
    print("I'm going to print with or without an error")
