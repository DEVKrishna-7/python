print("string data type")
"""
A String (str) is a sequence of Unicode characters used to store and represent text-based information. 
Think of it as a "string" of individual characters tied together.

1. The Core Characteristics :

Immutable: Once you create a string, you cannot change its characters in place. 
            Any "modification" actually creates a brand-new string in memory.

Ordered Sequence: Each character has a specific position (index), starting from 0.

Iterables: You can loop through a string character by character using a for loop.

2. How to Create Strings
    You can define strings using three types of quotes:
    Single/Double Quotes: 'Hello' or "Hello" (No functional difference).
    Triple Quotes: '''Hello''' """ """". Used for multi-line strings or 
    Docstrings (documentation inside code).

3. Key String Operations
    Indexing: Access a single character. name[0] gets the first letter.
    Slicing: Get a portion of the string. name[1:4] gets characters from index 1 to 3.
    Concatenation: Join strings using the + operator. "Python" + " is cool".
    Repetition: Repeat a string using *. "Hi" * 3 ---> "HiHiHi".

4. Escape Characters
Use the backslash "\" to include "illegal" characters:
\n: New line
\t: Tab
\': Single quote inside a single-quoted string.

5. Methods of String
['__add__',         '__class__',            '__contains__',         '__delattr__',     '__dir__', 
'__doc__',          '__eq__',               '__format__',           '__ge__',          '__getattribute__', 
'__getitem__',      '__getnewargs__',       '__getstate__',         '__gt__',          '__hash__', 
'__init__',         '__init_subclass__',    '__iter__',            '__le__',           '__len__', 
'__lt__',           '__mod__',              '__mul__',              '__ne__',          '__new__', 
'__reduce__',       '__reduce_ex__',        '__repr__',             '__rmod__',         '__rmul__', 
'__setattr__',      '__sizeof__',           '__str__',              '__subclasshook__', 

'capitalize',       'casefold',         'center',       'count',        'encode', 
'endswith',         'expandtabs',       'find',         'format',       'format_map', 
'index',            'isalnum',          'isalpha',      'isascii',      'isdecimal', 
'isdigit',          'isidentifier',     'islower',      'isnumeric',    'zfill'
'isprintable',      'isspace',          'istitle',      'isupper',      'join', 
'ljust',            'lower',            'lstrip',       'maketrans',    'partition', 
'removeprefix',     'removesuffix',     'replace',      'rfind',        'rindex', 
'rjust',            'rpartition',       'rsplit',       'rstrip',       'split', 
'splitlines',       'startswith',       'strip',        'swapcase',     'title', 
'translate',        'upper', ]

"""
s = "In Python a String str is a sequence of Unicode characters used to store and represent text based information by 1345 and @ and #$%&*."
u=s.upper()     # string convert into upper case.
print(u)

l=s.lower()     # string convert into lower case
print(l)

sw=s.swapcase() # swap the case upper to lower and lower to upper
print(sw)

c=s.capitalize()    # Only First element of string is upper case
print(c)

t=s.title()
print(t)        # First element of each word is upper case

""" all above method return output in string format"""

ia=s.isalnum()      #
print(ia)

iap= s.isalpha()
print(iap)

id = s.isdigit()
print(id)

iu=s.isupper()
print(iu)

iu=s.islower()
print(iu)

iss=s.isspace()
print(iss)

""" all above method return output in bool format"""

ind = s.index("In")
print(ind)

st=s.split()
print(st)
