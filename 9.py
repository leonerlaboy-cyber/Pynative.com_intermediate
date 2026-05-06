entry = [1, 2, 2, 3, 1, 4, 2]

def remove_duplicates(entry):

    clean_entry = []

    for i in entry:
        if i not in clean_entry:
            clean_entry.append(i)
    print(clean_entry)

remove_duplicates(entry)