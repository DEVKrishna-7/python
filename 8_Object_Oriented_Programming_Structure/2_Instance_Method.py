print("Instance method")
"""
The function inside the class is called method.

There are three types of  methods
1. instance method
2. class method
3. static method

1. Instance method
instance mean object.
A method it will present inside the class that work only on object.
in instance method by default parameter is "self".
instance method allways pointing to object.
we can call instance method outside the class using
class name and object
"""

class Practice:
    def instance_method(self):
        print("instance method")
obj=Practice()      # calling instance method by using object
obj.instance_method()       # calling instance method by using object
Practice.instance_method(obj)       # calling instance method by  sing

# instance method without argument
class Employee:
    def salary_cal(self):  # no argument in instance method
        sal=8000        # class variable
        print(f"your total salary is {sal}")
e=Employee()
e.salary_cal()      # call instance method by object
Employee.salary_cal(e)       # call instance method by class name.

# instance method with argument
class Employee:
    def salary_cel(self,salary):    # instance method have one argument is salary
        print(f"monthly salary is{salary+1000}")
e=Employee()
e.salary_cel(75000)  # pass the parameter

# using class variable in instance method
class Animal:
    species="Dog" # class variable
    oth_species="Cat" # class variable
    def sound(self):
        print(f"{self.species} barks") # calling class variable inside the method using self
        print(f"{Animal.oth_species} meow") # calling class variable inside the method using class name
a=Animal()
a.sound()
"""accessing class variable inside the method without self or class name or accessing directly then show NameError"""

# Accessing class variable inside the method by self and modifying by class name and object.

class Qspider:
    rating="1"
    sub="SQL"
    def Mock_rating(self):
        print(f"you are mock rating is {self.rating} in {self.sub} subject")
q=Qspider()
q.Mock_rating()
# modification done by class name
Qspider.sub="Python"
Qspider.rating="*"
q.Mock_rating()
# modification done by object
q.sub="Manual"
q.rating="1"
q.Mock_rating()

""" if we access the class variable inside the instance method by self thin we can do modification by class name and object.
but if we access the class variable inside the instance method by class name then we can not do modification by object it only done by class name."""
