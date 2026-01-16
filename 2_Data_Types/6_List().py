print("list data type")
"""
A List is Python’s most versatile and frequently used data structure. 
It is an ordered, mutable (changeable) collection that allows you to store multiple 
items in a single variable. 

1. Key Characteristics
Mutable: You can change, add, or remove items after the list is created.
Ordered: It maintains the specific order of insertion. Items are accessed by an index starting at 0.
Dynamic: Lists can grow or shrink in size as needed.
Heterogeneous: A single list can contain different data types (e.g., [1, "Hello", 3.14]). 
Indexing & Slicing

2. Syntax & Creation
Lists are defined using square brackets [].

3. Essential List Operations
Accessing: fruits[0] returns "apple".
Slicing: fruits[0:2] returns ["apple", "banana"].
Updating: fruits[1] = "mango" changes the second item.
Checking Length: Use the len() function to see how many items are inside. 

4. List Comprehension (Pro Tip)
This is a concise way to create lists. It’s faster and more "Pythonic" than 
using a standard for loop:

5. methods of list
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', 
'__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
'__iter__', '__le__', '__len__', '__lt__', '__mul__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', 
'__str__', '__subclasshook__', 

'append',   'clear',    'copy',     'count',    'extend', 
'index',    'insert',   'pop',      'remove',   'reverse', 
'sort']

"""
l=[1,1,1,2,2,2,2,3,4,5,6,7,8,9,0]
print("append list: ")
l.append(10)        # add element at last in list
print(l)           # output: [1, 1, 1, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]

a=l.append(11)
print(a)            # output: None

print("count list:")
c=l.count(2)        # no. of count of element present in list
print(c)

print("insert element in list: ")
l.insert(0,0.5)     # add element in particular using  index position
print(l)

print("Pop element in list: ")
l.pop()     # remove last element in list
print(l)

print("reverse list: ")
l.reverse()     # change list order ascending <----------> descending
print(l)

print("count of list: ")
l.count(2)
print(l)

print("Extend list: ")
l.extend([12,12,13]) # add iterable/ collection of data at last in list
print(l)

print("index of list")
i=l.index(1)        # show index position of element in list
print(i)

l.sort() # sort the element
print(l)

l.clear() # remove all elements from list
print(l)

l2=["Python","java","c++","c","sql","Plsql","Html","css","javascript"]


"""
-------------------------Types of copy------------------------------------
1. copy : same address of store data 
2. shallow copy : use copy() method. different  of store data
3. deep copy : 
4. Nested shallow copy : List inside list. different address od store data
"""
# Normal Copy
l=[1,1,1,2,2,2,2,3,4,5,6,7,8,9,0]
l=a
print(id(l))
print(id(a))

# Shallow copy
l=[1,1,1,2,2,2,2,3,4,5,6,7,8,9,0]
y=l.copy()
print(y)
print(id(l))
print(id(y))

# Nested copy
k=[1,2,3,[4,5,6],7]
v=k.copy()
print(id(k))
print(id(v))

# deep copy
from copy import deepcopy
l=[1,1,1,2,2,2,2,3,4,5,6,7,8,9,0]
n=deepcopy(l)
print(n)
print(id(l))
print(id(n))