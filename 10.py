from collections import deque

def rotate_list(lst, n, direction):

    lst = deque(lst)
    
    if direction.lower() == 'right':
        lst.rotate(n)
    else:
        lst.rotate(-n)
    print(list(lst))

my_list, shift, direction = [1, 2, 3, 4, 5], 2, 'right'
rotate_list(my_list, shift, direction)
rotate_list(my_list, 1, 'left')

# expected: [4, 5, 1, 2, 3]
# 'right' = clockwise, 'left' = counter clockwise

#'Normal' version

# def rotate_list(lst, n, direction='right'):
#     if not lst:
#         return lst
        
#     # Handle shifts larger than the list length
#     n = n % len(lst)
    
#     if direction == 'right':
#         # Take the last n elements and put them at the front
#         return lst[-n:] + lst[:-n]
#     else:
#         # Take the first n elements and put them at the back
#         return lst[n:] + lst[:n]

# # Usage
# data = [1, 2, 3, 4, 5]
# print(f"Right Shift 2: {rotate_list(data, 2, 'right')}")
# print(f"Left Shift 1:  {rotate_list(data, 1, 'left')}")