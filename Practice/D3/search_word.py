with open("Practice/D3/sample.txt", "r") as f:
    text = f.read().lower()

word = input("Enter the word you want to find: ").strip().lower()

words_list = text.split()
count = 0

for w in words_list:
    if w == word:
        count += 1

if count == 0:
    print("Word not found!")
else:
    print(word, "found", count, "times")
