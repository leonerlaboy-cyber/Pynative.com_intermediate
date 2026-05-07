d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

def merge_and_group(dict1, dict2):
    combined = {}
    # Get all unique keys from both dictionaries
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    # print(all_keys)
    
    for key in all_keys:
        values = []
        if key in dict1:
            values.append(dict1[key])
        if key in dict2:
            values.append(dict2[key])
        combined[key] = values
        
    return combined

print(f"Grouped Merge: {merge_and_group(d1, d2)}")
