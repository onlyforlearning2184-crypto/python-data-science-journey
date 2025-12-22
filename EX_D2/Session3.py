# Basic set

nums = {1, 2, 3}
nums.add(4)
print(nums)
nums.add(2)
print(nums)

# Membership test
animals = {"cat", "dog", "cow"}
user = input("Enter the animal name : ").strip().lower()
if user in animals:
    print(user, "is found in Animals")
else:
    print(user, "does not found in Animals")

# Set Update
s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1.update(s2)
print(s1)

# Union
a = {10, 20, 30}
b = {30, 40, 50}

c = a.union(b)
print(c)

# intersection
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.intersection(set2))
