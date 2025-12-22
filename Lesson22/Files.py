import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it dosent't exist

f = open("names.txt")
# print(f.read())
# print(f.read(5))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

# try:
#     f = open("dave.txt")
#     print(f.read())
# except FileExistsError:
#     print("The file you want to read dosen't exist")
# finally:
#     f.close()

# Append - creates the file if it dosen't exist
f = open("names.txt", "a")
f.write("Neil")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I delete all of the content")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Open a file for writing, creates the file if it does not exist

f = open("name_list.txt", "w")
f.close

# Creates the specified file, but returns an error if the file exists

if not os.path.exists("rachit.txt"):
    f = open("rachit.txt", "x")
    f.close()

# Delete a file

# avoid an error if it does't exist

if os.path.exists("rachit.txt"):
    os.remove("rachit.txt")
else:
    print("The file you wish to delete does not exist")


with open("names.txt") as f:
    content = f.read()

with open("more_names.txt", "w") as f:
    f.write(content)
