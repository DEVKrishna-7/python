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

# Real world example
# Parent Class: Basic features for all bank accounts
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def display_balance(self):
        print(f"Owner: {self.owner} | Balance: ${self.balance}")


# Child Class: Adding specialized "Savings" features
class SavingsAccount(BankAccount):
    # This class automatically gets owner and balance from BankAccount

    def add_interest(self, rate):
        """Calculates interest and updates the balance."""
        interest = (self.balance * rate) / 100
        self.balance += interest  # Updates the balance inherited from parent
        print(f"Interest Added: +${interest}")


# --- Testing the Code ---

# 1. Create a SavingsAccount for "John" with $1000
# Note: It uses the Parent's __init__ because we didn't write a new one
john_savings = SavingsAccount("John", 1000.0)

# 2. Call inherited method
john_savings.display_balance()  # Output: Owner: John | Balance: $1000.0

# 3. Call child-specific method (5% interest)
john_savings.add_interest(5)  # Output: Interest Added: +$50.0

# 4. Final balance check
john_savings.display_balance()  # Output: Owner: John | Balance: $1050.0
