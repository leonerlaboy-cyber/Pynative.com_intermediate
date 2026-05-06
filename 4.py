word1, word2  = "listen", "silent"

def anagram(word1, word2):

    if sorted(word1) == sorted(word2):
        print(f'{word1} is an anagram of {word2}')
    else:
        print(f'{word1} is NOT an anagram of {word2}')

anagram(word1, word2)
anagram('dog', 'god')
anagram('frog', 'goat')