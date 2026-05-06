from collections import Counter

my_dict = "This is a test of counter.".replace(" ", "").lower()

result = dict(Counter(my_dict))

print(result)