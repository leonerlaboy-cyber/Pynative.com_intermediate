a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

def validation(lst1, lst2):

    if lst1 < lst2: 
        print(f'Set A is a subset of set B') #Checks if a is subset of b

    if lst2 > lst1: 
        print(f'Set B is a superset of set A') #Checks if b is superset of a

    if not (a & b):
        print('The sets are disjoint (they share no elements).') #Checks if a and b have all unique values. Returns false if they share a single value. 
    else:
        print(f'The sets share these elements: {lst1 & lst2}')

validation(a, b)
