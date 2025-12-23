f = open("Practice\D3\sample.txt", "r")
text = f.read()
line_count = len(text.splitlines())
word_count = len(text.split())
char_count = len(text)
# line_count = 0
# word_count = 0
# char_count = 0

# for char in f.read().strip():
#     char_count += 1


# for line in f.readlines():
#     line_count += 1


# for word in f.read().split():
#     word_count += 1

print("Lines :", line_count)
print("Words :", char_count)
print("Characters :", word_count)
