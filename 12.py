authors = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}

def invert_dict(entry):

    switched = {}

    for authors, books in entry.items():
        for book in books:
    print(switched)

invert_dict(authors)