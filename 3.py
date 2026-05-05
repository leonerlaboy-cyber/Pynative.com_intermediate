from collections import Counter

def get_frequency(input_string):
    # Clean the string: remove spaces and lowercase everything
    clean_text = input_string.lower().replace(" ", "")
    
    # Counter automatically builds the frequency map
    return Counter(clean_text)

text = "Python Programming"
freq = get_frequency(text)

print(f"Original: {text}")
print(f"Character Frequency: {freq}")
    
