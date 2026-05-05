dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}

def merg_dict(d1, d2):

    result = d1.copy()

    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result

merged = merg_dict(dict_a, dict_b)

print(f'Merged Dictionary: {merged}')
