## 1. Remove all spaces from a string

# string = str(input("Enter a sentance : "))
# print("Before removing the spaces : ", string)

# new_st = ""
# for char in string:
#     if char == " ":
#         continue
#     else:
#         new_st += char

# print("After removing the spaces : ", new_st)

# # OR
# string = input("Enter a sentence: ")
# new_st = string.replace(" ", "")
# print(new_st)

# # 2️⃣ Count how many uppercase and lowercase letters are in a string
# sent = str(input("Enter the string : ")).strip()
# count_upper = 0
# count_lower = 0

# for char in sent:
#     if char.isupper():
#         count_upper += 1
#     if char.islower():
#         count_lower += 1


# print("Uppercase : ", count_upper)
# print("Lowercase : ", count_lower)


# # Replace all vowels with *

# string = str(input("Enter a string : ")).strip()

# vowels = "aeiouAEIOU"

# new_string = ""
# for char in string:
#     if char in vowels:
#         new_string += "*"
#     else:
#         new_string += char

# print(new_string)

# # 4️⃣ Take a name as input and print it in Title Case
# full_name = str(input("Enter the name : ")).strip()
# new = full_name.split()
# new_words = []

# for word in new:
#     changed = word[0].upper() + word[1:].lower()
#     new_words.append(changed)

# re = " ".join(new_words)
# print(re)


# # 5️⃣ Get the last 3 characters of a string using slicing
# string = str(input("Enter the string : ")).strip()
# print(string[-3:])  # or string[-3:] + string[-2] + string[-1]

# # 6️⃣ Remove duplicates from a list without using set() and without using list comprehension
# li = [1, 2, 2, 3, 3, 3, 4]
# new_li = []
# for num in li:
#     if num not in new_li:
#         new_li.append(num)
#    # else:
#    #     continue
# print(new_li)


# # 7️⃣ Write a function that returns the 2nd largest number in a list
# def second_largest(nums):
#     larg = nums[0]
#     for n in nums:
#         if n > larg:
#             larg = n
#     sec = None
#     for n in nums:
#         if n != larg:
#             if sec is None or n > sec:
#                 sec = n
#     return sec


# print(second_largest([1, 20, 4, 12, 19, 7]))


# 8️⃣ Merge two dictionaries
a = {"name": "Tirth"}
b = {"age": 18}

new = {}

for el in a:
    new[el] = a[el]


for el in b:
    new[el] = b[el]

print(new)
