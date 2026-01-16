print("set data type")
"""
A Set is an unordered collection of unique elements. 
It’s the go-to tool when you want to eliminate duplicates or perform mathematical 
operations like unions and intersections. 
1. Key Characteristics
Uniqueness: It automatically removes duplicate values. If you add "apple" twice, it only stays once.
Unordered: Items have no defined order. You cannot access them via my_set[0].
Mutable: You can add or remove items, but the items themselves must be hashable (immutable).
No Indexing/Slicing: Because it's unordered, position-based access isn't possible. 

2. Syntax & Creation
Sets use curly braces {}, just like dictionaries, but without key-value pairs. 

3. Powerful Mathematical Operations
Sets shine when comparing two groups of data. This is often faster than using loops. 

Union (|): Combines elements from both (no duplicates).
Intersection (&): Only keeps elements found in both.
Difference (-): Keeps elements in the first set but not the second.
Symmetric Difference (^): Keeps elements in either set, but not both. 
Check the Python Set Documentation for the full list of operators.

4. methods of set:
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', 
'__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', 
'__ixor__', '__le__', '__len__', '__lt__', '__ne__', 
'__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', 
'__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', 
'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 


'add',      'clear',        'copy',         'difference',       'difference_update', 
'discard',  'intersection', 'intersection_update',  'isdisjoint',   'issubset', 
'issuperset',   'pop',  'remove', 'symmetric_difference', 'symmetric_difference_update', 
'union',    'update'
]

"""
s={1,2,3,4,5,6,7,8,9,0,11,12}
print(s)
s.add(54)
print(s)
print(type(s))
print(s)

s.pop()     # remove element form begging
print(s)

s.remove(5) # remove particular give element in set
print(s)
s={1,2,3,4,5,6,7,8,9,0,11,12}
s1={5,4,6,8,7,3,9,100,500}
s.update(s,s1)
print(s)

s.union(s,s1)
print(s)

s.clear()       # remove all the elements in set.
print(s)

