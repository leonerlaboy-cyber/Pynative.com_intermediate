sentence = "A man, a plan, a canal: Panama"

def palindrome(phrase):

    clean_chars = [char.lower() for char in phrase if char.isalnum()]
    
    clean_str = "".join(clean_chars)

    if clean_str == clean_str[::-1]:
        print('This is a palindrome')
    else:
        print('This is NOT a palindrome')

palindrome(sentence)
palindrome('Bunny')

# sentence = "A man, a plan, a canal: Panama"

# clean_phrase = sentence.lower().strip()
# print(clean_phrase) 