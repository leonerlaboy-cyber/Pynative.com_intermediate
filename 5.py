def flatten(nested):
    result = []

    for item in nested:
        if isinstance(item, list):      # if it's a list, dig in
            result += flatten(item)     # call itself on the inner list
        else:                           # if it's a number, keep it
            result.append(item)

    return result

nested = [1, [2, 3], [4, [5, 6]], 7]
print(f"Flattened: {flatten(nested)}")