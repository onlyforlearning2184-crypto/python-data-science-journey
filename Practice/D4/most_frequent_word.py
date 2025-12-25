with open("Practice/D3/sample.txt", "r") as f:
    text = f.read().lower()

words_list = text.split()
word_dict = {}

# count frequency
for word in words_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

# find most frequent word
max_count = 0
most_frequent = ""

for word in word_dict:
    if word_dict[word] > max_count:
        max_count = word_dict[word]
        most_frequent = word

print("Most frequent word:", most_frequent)
print("Count:", max_count)
