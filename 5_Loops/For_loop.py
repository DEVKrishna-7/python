from itertools import zip_longest

print("for loop")
x="Python"
for i in x:
    print(i)
# -----------------------------------------------------------------------------
# reversed (): use to reversed iterable except set. because set is unordered
print(reversed(x)) # return reversed object address

print(list(reversed(x))) # return output in list format because we use type casting.

for i in reversed(x):   # return output in reverse format and unpacked format.
    print(i)

a = ["jan", "feb", "mar", "apr", "may", "june"]
for i in a:
    print(i)

# enumerate()
print(enumerate(a)) # return enumerate object address

print(list(enumerate(a))) # return output in form of list

for i in enumerate(a):
    print(i)

# zip
for i in zip(a,x):
    print(i)

# zip_logest

for i in zip_longest([1,2,3,4,5],["a","b","c","d"]):
    print(i)

for i in zip_longest([1,2,3,4,5],["a","b","c","d"],fillvalue="Zero"):
    print(i)

# range()
for i in range(1,9):
    print(i)