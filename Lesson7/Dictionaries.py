# Dictionary
# Key-values
# band = {
#     "Vocals": "Plant",
#     "Guitar": "Page",
# }
band2 = dict(Vocals="Plant", Guitar="Page")

# print(band)
# print(type(band))
# print(band2)
# print(type(band2))
# print(len(band))

# Access items
# print(band["Vocals"])
# print(band.get("Guitar"))  # method

# list all keys/values
# print(band.keys())
# print(band.values())

# list of key values pair as tuples
# print(band.items())

# Varify a key exists
# print("Guitar" in band)
# print("guitar" in band)

# change values using key
# band["Vocals"] = "Coverdale"
# print(band)

# Adding
# band.update({"Bass": "JPJ"})
# print(band)

# removing
# print(band.pop("Bass"))
# print(band)

# band["Drums"] = "Bonham"
# print(band)

# print(band.popitem())  # tuple
# print(band)


# Delete / clear
# band["Drums"] = "Bonham"
# del band["Drums"]
# print(band)

band2.clear()
# print(band2)

del band2

# Copy
# band2 = band  # Create reference means both are connected
# print("Bad copy!")
# print(band)
# print(band2)

# band2["Drums"] = "Dave"
# print(band)
# print(band2)

# band2 = band.copy()
# band2["Drums"] = "Dave"
# print("Good copy!")
# print(band)
# print(band2)


# or use cunstructor
# band3 = dict(band)
# print("Good copy!")
# print(band)
# print(band2)

# nested dictonary
member1 = {"name": "Plant", "instrument": "Vocals"}
member2 = {"name": "Page", "instrument": "guitar"}
band = {"member1": member1, "member2": member2}

print(band)
print(band["member1"]["name"])

# Sets
nums = {1, 2, 3, 4, 5}
num2 = set((1, 2, 3, 4))

print(nums)
print(num2)
print(type(nums))
print(len(nums))

# no Dupluicate allows (Constant values only allows)
# auto sort
nums = {1, 1, 2, 2, 3, 4, 5, 6, 5, 7}
print(nums)

# True is a duplicate of 1, False is a duplicate of zero
num = {1, True, 2, False, 3, 4, 0}
print(num)

# check if a value is in a set
print(2 in num)

# but you cannot refer to an element in the set with an index position or a key


# adding
num.add(8)
print(num)

# from 1 set to another
more_nums = {5, 6, 7}
num.update(more_nums)
print(num)

# you can use update with lists, tuples, and dictionaries, too.

# merge two sets to create a new set

one = {1, 2, 3}
two = {5, 6, 7}

my_new_sets = one.union(two)
print(my_new_sets)

# keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)


# keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)


# use . notation for any available methods in any data type
