# Tuples
# Data inside cannot be changed and order of the data will not change

my_tuple = tuple(("Dave", 42, True))  # you can use multiple datatype in tuple
another_tuple = (1, 4, 2, 8)

print(my_tuple)
print(type(my_tuple))
print(another_tuple)
print(type(another_tuple))

# us can use cunstructure to copy the tuple and then modify it then change it to tuple
new_list = list(my_tuple)
new_list.append("Neil")
new_tuple = tuple(new_list)
print(new_tuple)

# unpacking the tuple into the variables

(one, *two, hey) = another_tuple
print(one)
print(two)
print(hey)
