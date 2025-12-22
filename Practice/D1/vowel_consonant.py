string = str(input("Enter the string : ")).strip()
vowels = "aeiouAEIOU"
count_vov = 0
count_con = 0

for char in string:
    if char == " ":
        continue
    elif char.isalpha():
        if char in vowels:
            count_vov += 1
        else:
            count_con += 1

print(f"\nVovels : {count_vov}")
print(f"\nConsonant : {count_con}")
