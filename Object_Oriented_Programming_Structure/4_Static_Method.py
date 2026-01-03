print("static method")
"""
Any method it will present inside the class and decorated with @staticmethod
the static method take self and cls parameter
it's also know as independent method
we can not done any modification by object and class name but we can do manually
it use for maintain code structure
"""
class Math:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def greet(name):
        print(f"hellow,{name}!")

print(Math.add(10,20))
Math.greet("pydev")

class Demo:
    @staticmethod
    def add():
        print("i am static method")
d=Demo()
d.add()     # accessing static method by object
Demo.add()      # accessing static method by class name.

class Calculator:
    a=10
    b=20
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod
    def div(a,b):
        return a/b
c=Calculator()
print(c.add(10,5))
c.sub(10,5)
Calculator.mul(10,5)
Calculator.div(10,5)
""" if we try any modification by calss and object it's not effect on static method
because it not associated with class and object."""