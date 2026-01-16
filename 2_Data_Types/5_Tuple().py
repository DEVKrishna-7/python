print("Tuple data type")
"""
A Tuple is essentially a "locked" version of a list. It is an ordered, immutable collection, meaning once you define it, 
you cannot add, remove, or change its items. 

Think of it as a permanent record—perfect for data that should never change, like GPS coordinates or a person's date of birth. 

1. Key Characteristics

Immutable: This is the most important feature. If you try to change an element (e.g., my_tuple[0] = 5), Python will raise a TypeError.
Ordered: It maintains the sequence of elements.
Allows Duplicates: You can have the same value multiple times.
Heterogeneous: It can store a mix of different data types (ints, strings, even lists). 

2. Syntax & Creation
Tuples use parentheses () instead of square brackets.

3. Why use a Tuple instead of a List?
Safety: It protects your data against accidental changes.
Performance: Tuples are slightly faster and more memory-efficient than lists.
Hashability: Because they are immutable, tuples can be used as Dictionary Keys (as long as they contain only immutable objects). 

4. Methods of tuple:
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__mul__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', 


'count',    'index'
]

"""
t=(1,1,1,2,2,3,4,5,6,7,8,9,0)
c=t.count(1)
print(c)

i=t.index(1)
print(i)
