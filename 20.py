from collections import namedtuple

# def print_info(**kwargs):

#     print(kwargs)


# print_info(name="Alice", age=30, city="New York")

# my_tuple = ("apple", "banana", "cherry", "date", "cherry")

# # print(my_tuple.count("cherry"))
# print(my_tuple.index("cherry")) #finds first instance of cherry
# print(my_tuple.index("cherry", 3)) #finds first instance after from index 3 on

# person = namedtuple('person', ['name', 'age', 'city'])

# me = person('alex', 20, 'dover')

# print(me)

# my_tuple = (3, 1, 4, 1, 5, 9)

# sorted_tuple = tuple(sorted(my_tuple)) #need to use tuple() before sorted because sorted returns a list not a tuple
# print(sorted_tuple)

# user_likes = {'action', 'comedy', 'drama', 'thriller'}
# available = {'comedy', 'drama', 'fantasy', 'sci-fi', 'action'}
# friends_like = {'comedy', 'horror', 'drama', 'thriller'}

# user_like_available = user_likes & available
# print(user_like_available)

# available_not_interested = available - user_likes
# print(available_not_interested)

# user_friends_like = user_likes & friends_like
# print(user_friends_like)

# available_friends_nouser = (available & friends_like) - user_likes
# print(available_friends_nouser)

in_stock = {'apple', 'banana', 'orange', 'grape', 'peach'}
reorder = {'banana', 'peach', 'kiwi', 'melon'}
on_sale = {'apple', 'orange', 'melon', 'grape'}

print(f'{in_stock & on_sale} are in stock and on sale')
print(f'{reorder - on_sale} need to be restocked and are not on sale')
print(f'{on_sale < in_stock}: Not all items on sale are in stock')
print(f'{reorder - in_stock}')