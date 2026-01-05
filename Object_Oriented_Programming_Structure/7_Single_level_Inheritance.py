from pyexpat import native_encoding

print("Single Level Inheritance")
"""
Inheritance: Acquiring property from one class to another class.

Single Level Inheritance:
child class Acquiring property from parent class OR child class take property from parent class
"""
class Parent1:
    bla="30 LPA"
    def house(self):
        print("parent house")
class child(Parent1):
    def studying(self):
        print("child still study")

c=child()
c.bla
c.house()
c.studying()

# Real world example: Employee ----> Manager
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def details(self):
        print(f"name: {self.name} \nsalary is {self.salary}")

class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size
    def details(self):
        super().details()
        print("Manages team of",self.team_size)

m=Manager("riya",9000000,5)
m.details()