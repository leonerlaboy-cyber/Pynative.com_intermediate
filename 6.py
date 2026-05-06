sentence = "Python is awesome"

words = sentence.split()
reversed_words = []

for word in words:
    word = word[::-1]
    reversed_words.append(word)
print(" ".join(reversed_words))
    