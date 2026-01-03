print("Object Oriented Programming_Structure/ System (OOP's)")
"""
A real world object convert into software world is called OOP

use of oop's
easy to store data in organized way
easy to access the data
for re-usability purpose
for maintainability purpose

Clss: it is act plan / blue print / model / design of the object.
object: it is instance of class
        0bject is real world entity which have it's won attributes and property.
        object is pointing to class.
        
There are three member of inside the class
1. Methods
2. Constructor
3. Variables

There are Three types of variables
1. class variable / static variable
2. local variable
3. instance variable
"""
# inside class data print outside directly it will show NameError
class Employee:
    eid = 420
    ename="Pydev"
    gender="Male"
# print(eid)      # NameError: name 'eid' is not defined.

"""Accessing class variable by using class name"""
print(Employee.eid)         # Employee is class name and eid is class variable.
print(Employee.ename)
print(Employee.gender)
"""object creation"""
e= Employee # without bracket, it shows main class
print(e) # <class '__main__.Employee'>

e=Employee() # with bracket, it shows main class object address
print(e) # <__main__.Employee object at 0x000002441A576F90>

"""Accessing class variable by using object"""
print(e.eid)        # e is object and eid is class variable
print(e.ename)
print(e.gender)

""" Create Empty class"""
class Demo:
    pass        # Using pass keyword create empty class.

class Spam:
    ...         # Using ... three dots create empty class.

"""Documentation String / Doc String"""
class Ipl:
    """Team details"""
    team = 'RCB'
    capton = "virat"
    j_no = 18
print(Ipl.__doc__) # __doc__ is a magic method. use to get description in title format.

""" help is a function use to get all detail description of class"""
help(Ipl)

print(Ipl.__dict__)     # __dict__ is a magic method. use to see how data stored internally
                        # in class data stored in key: value pair / Dictionary format


class Mod:
    a=10
    b=20
d1=Mod()
d2=Mod()
print(Mod.a) # class variable call by class name
print(Mod.b) # class variable call by class name
print(d1.a) # class variable call by object d1
print(d1.b) # class variable call by object d1
print(d2.a) # class variable call by object d2
print(d2.b) # class variable call by object d2

Mod.a= 100 # modify class variable value by class name
print(Mod.a)  # effect on class
print(d1.a)     # effect on object d1
print(d2.a)     # effect on object d2

d1.a=11     # modifu class variable value by using object
print(Mod.a)    # effect not on class
print(d1.a)     # effect only on object d1
print(d2.a)     # effect not on object d2

Mod.a=1100 # modify class variable value again by using class name
print(Mod.a)    # effect on class
print(d1.a)     # effect not on object d1 because we loos connectivity
print(d2.a)     # effect on object d2