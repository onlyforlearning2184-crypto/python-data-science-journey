name = "Tirth"  # Globle  variable


# def greeting(name):
#     color = "red"  # Local variable
#     print(color)
#     print(name)
#     # return name, color


# greeting("tirt")
# # another = greeting()
# # print(color)

count = 1


def another():
    color = "red"  # Local variable
    # count = 2  # new variable insted of the global variable with same name
    # global count = 2 # Error
    global count  # modifying global function
    count += 1
    # count += 1
    print(count)

    def greeting(name):
        nonlocal color  # it tell that we using the color from the parent function
        color = "red"
        print(color)
        print(name)
        # return name, color

    greeting("Dave")


another()

# another = greeting()
# print(color)
