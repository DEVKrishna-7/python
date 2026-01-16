print("Collection data type")
# string data type
s = "Python is programming language"
"""
string data type boundaries are "" / ''
"""
# list data type
l = [1, 2, 3, 4, 5, 6]
l=["a","b","c","d","e","f","g"]

# tuple Data type
t= (1, 2, 3, 4, 5, 6)
t=("a","b","c","d","e","f","g")

# set data type
s={1,2,3,4,5,6,7}

# dictionary data type
d={1:"jan",2:"feb",3:"mar",4:"apr",5:"may",6:"jun"}



# -----------------------------------------------------------

"""
Iterable : All collection data type also known as iterable.

Hashable/Immutable (Unchangeable) : Once created, the value cannot be modified. If you try to change it, Python creates a new object in memory.
Types: int, float, bool, str, tuple.
Hashable:
Must be immutable.
Can be used as a Dictionary Key or an element in a Set.
Python uses the hash() function to turn these objects into a fixed integer.
Examples: str, int, tuple (only if the tuple contains hashable items).


Unhashable/Mutable (Changeable): You can change the contents of the object without changing its identity (its address in memory).
Types: list, dict, set.
Unhashable:
Usually mutable.
Cannot be used as a Dictionary Key because their "identity" might change if their content changes.
Examples: list, dict, set.

"""