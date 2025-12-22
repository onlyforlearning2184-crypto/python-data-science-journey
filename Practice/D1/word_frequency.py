sentence = str(input("Enter the sentance : ")).strip().lower()

new_sen = {}

words = sentence.split()

for word in words:
    if word in new_sen:
        new_sen[word] += 1
    else:
        new_sen[word] = 1

print(new_sen)
