print("Slicing")
"""
Slicing:
        The process of fetching multiple characters/Element is called Slicing.
        In slicing we have three types
        1. positive Slicing
        2. negative Slicing
        3. combination Slicing (+ve,-ve and -ve,+ve)
        
        syntax: [start_index : end_index+1 : step_value]
        positive Slicing :
                            start_index ---> default value is 0
                            end_index -----> default value length of collection
                            step_value -----> default value is 1
        
        negative Slicing :
                            start_index ---> default value is -1
                            end_index -----> default value -(length of collection)
                            step_value -----> default value is -1
            note: step value is allways negative
"""
# String Data type
x= "Python programing language"
# Positive Slicing
print(x[::])
print(x[1:6:2])
# Negative Slicing
print(x[::-1])
print(x[-2:-8:-3])
print("-------------------------------------------------")

# List data type
l=[1,2,3,4,5,6,7,8,9,0]
# Positive Slicing
print(l[::])
print(l[1:6:2])
# Negative Slicing
print(l[::-1])
print(l[-2:-8:-2])

l=["a","b","c","d","e","f","g"]
# Positive Slicing
print(l[::])
print(l[1:6:2])
# Negative Slicing
print(l[::-1])
print(l[-2:-8:-2])
print("-------------------------------------------------")

# tuple data type
t=(1,2,3,4,5,6,7,8,9,0)
# Positive Slicing
print(t[::])
print(t[1:6:2])
# Negative Slicing
print(t[::-1])
print(t[-2:-8:-2])

t=("a","b","c","d","e","f","g")
# Positive Slicing
print(t[::])
print(t[1:6:2])
# Negative Slicing
print(t[::-1])
print(t[-2:-8:-2])
print("-------------------------------------------------")

# set data type
s={1,2,3,4,5,6,7,8,9,0}
# Positive Slicing
# print(s[::])
# print(s[1:6:2])
# Negative Slicing
# print(s[::-1])
# print(s[-2:-8:-2])
""" set does not support Slicing it show error is : TypeError: 'set' object is not subscriptable 
    because set is unordered.
"""
print("-------------------------------------------------")

# Dictionary data type
d={1:"jan",2:"feb",3:"mar",4:"apr",5:"may",6:"jun"}
# Positive Slicing
# print(d[::])
# print(d[1:6:2])
# Negative Slicing
# print(d[::-1])
# print(d[-2:-8:-2])
""" Dictionary does not support Slicing it show error is :KeyError: slice(None, None, None)
    because stored in key and value pair
 """