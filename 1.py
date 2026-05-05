words = ["apple", "bat", "cherry", "dog", "elderberry"]
# new_list = []

# for word in words:

#     if len(word) > 4:
#         new_list.append(word.upper())

new_list = [word.upper() for word in words if len(word) > 4]

print(new_list)
