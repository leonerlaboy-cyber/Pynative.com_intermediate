authors = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}

def invert_dict(entry):

    switched = {}

    for author, books in entry.items():
        for book in books:
            switched[book] = author
    return switched

print(f'Inverted index: {invert_dict(authors)}')