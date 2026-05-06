my_list = ["apple", "education", "ice", "ocean", "python", "umbrella"]

new_list = [word for word in my_list if len(word) > 5 and word[0].lower() in 'aeiou']

print(new_list)        
