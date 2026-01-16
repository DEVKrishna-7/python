print("dictionary data type")
"""
A Dictionary (dict) is Python's implementation of an associative array or hash map. 
It stores data in Key-Value pairs, making it incredibly fast for looking up 
information based on a specific label rather than a position. 

1. The Core Characteristics
Key-Value Structure: Every entry has a "Key" (the label) and a "Value" (the data).
Unique Keys: Keys must be unique and hashable (immutable types like strings, numbers, or tuples).
Mutable: You can add, remove, or change values after the dictionary is created.
Ordered (Since 3.7): While you access items by key, Python remembers the order in which items were inserted. 

2. Syntax & Creation
Dictionaries use curly braces {} with colons separating keys and values. 

3. Why use a Dictionary?
Dictionaries are optimized for speed. If you have 1 million items, 
finding a value by its key in a dictionary happens almost instantly, 
whereas searching a list would require checking every single item.

4. methods of dictionary
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', 
'__len__', '__lt__', '__ne__', '__new__', '__or__', 
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', 
'__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 

'clear',    'copy',     'fromkeys',     'get',          'items', 
'keys',     'pop',      'popitem',      'setdefault',   'update', 
'values']
"""

d= {'user_0': 21, 'user_1': 67, 'user_2': 47, 'user_3': 51, 'user_4': 13,
    'user_5': 57, 'user_6': 52, 'user_7': 93, 'user_8': 81, 'user_9': 92}

g=d.get('user_3')  # return value of key input is key in dict
print(g)

k=d.keys()  # return all keys in
print(k)

v=d.values()     # return all values
print(v)

i=d.items()     # return all key and value pari in tuple format.
print(i)

di=d.copy()
print(di)
print(id(d))
print(id(di))

d.clear()  # clear all element in dict
print(d)

import random

# Generate a dictionary with 10,000 unique ID keys and random scores
large_dict = {f"user_{i}": random.randint(1, 100) for i in range(10)}
# print(large_dict)
# Practice: Find all users with a score above 90
top_users = {k: v for k, v in large_dict.items() if v > 90}
# print(f"Total top users found: {len(top_users)}")
