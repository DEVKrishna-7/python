print("indexing")
"""
Indexing:
            The process of fetching single single character in collection data types is called Indexing
            Indexing we can do in two ways forward and backword
            forward direction (left to right) always start form zero.
            back word direction (right to left) always start from -1.
            
            Syntax: 
                    variable_name [index position/number]0
                    
            Note: If the given position is not present it will show index error.
            
            Input type as a Position/number ----------> Output type as a string
"""
# String Data type
x= "Python programing language"
# forward Indexing
print(x[0])
print(x[1])
print(x[2])
print(x[3])
# backword indexing
print(x[-1])
print(x[-2])
print(x[-3])

y="z"
print(y[0])
print(type(y))
print("-------------------------------------------------")

# List data type
l=[1,2,3,4,5,6,7,8,9,0]
# forward Indexing
print(l[0])
print(l[1])
print(l[2])
print(l[3])
# backword indexing
print(l[-1])
print(l[-2])
print(l[-3])

l=["a","b","c","d","e","f","g"]
# forward Indexing
print(l[0])
print(l[1])
print(l[2])
print(l[3])
# backword indexing
print(l[-1])
print(l[-2])
print(l[-3])
print("-------------------------------------------------")

# tuple data type
t=(1,2,3,4,5,6,7,8,9,0)
# forward Indexing
print(t[0])
print(t[1])
print(t[2])
print(t[3])
# backword indexing
print(t[-1])
print(t[-2])
print(t[-3])

t=("a","b","c","d","e","f","g")
# forward Indexing
print(t[0])
print(t[1])
print(t[2])
print(t[3])
# backword indexing
print(t[-1])
print(t[-2])
print(t[-3])
print("-------------------------------------------------")
# set data type
s={1,2,3,4,5,6,7,8,9,0}
# forward Indexing
# print(s[0])
""" set does not support indexing it show error is : TypeError: 'set' object is not subscriptable 
    because set is unordered.
"""
print("-------------------------------------------------")
# Dictionary data type
d={1:"jan",2:"feb",3:"mar",4:"apr",5:"may",6:"jun"}
# forward Indexing
# print(d[0])
""" Dictionary does not support indexing it show error is :KeyError: 0
    because stored in key and value pair
 """