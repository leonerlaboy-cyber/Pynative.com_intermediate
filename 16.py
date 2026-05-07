from itertools import combinations

lst = [1, 2, 3]

def power_set(lst):

    output = []
    
    for num in range(len(lst) + 1):
        for combo in combinations(lst, num):
            output.append(combo)
    print(output)


power_set(lst) 
