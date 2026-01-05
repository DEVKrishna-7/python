print("constructor")
"""
it is a special member of class
constructor defined by __init__()
constructor will get executed whenever we create an object/instance.
is used to initialize(assign values to) instance variable

There are two types of constructor
1. predefine/ default constructor
2. user define constructor
    i. with parameterized constructor
    ii. without parameterized constructor
"""
# default constructor
class Emp:
    name="abhi"
    def detail(self):
        print("welcome to the company")
e=Emp()
e.detail()
# the default constructor is present inside the class, but we can't see

# constructor without any argument
class Animal:
    def __init__(self):
        print("Welcome to zoo")
    def Sound(self):
        print("lion and tiger")
a=Animal()
a.Sound()

# user defined constructor
# without argument
class Students:
    def __init__(self):
        print("welcome student")
    def sem_1st(self):
        print("we are 1st sem students")
    def sem_3rd(self):
        print("we are seniors")
s=Students()
s.sem_1st()
s.sem_3rd()

# constructor with argument
class Details:
    def __init__(self,name,balance,add):
        acc_name=name
        acc_bal=balance
        acc_add=add
        print(f"my account name is {acc_name}\naccount balance is {acc_bal}\naccount address is {acc_add}")
d=Details("virat","18000000","London")
