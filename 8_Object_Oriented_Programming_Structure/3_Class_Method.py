print("class method")
"""
class method: Any method it will present inside the class that work only on class.
class method is always decorated with @classmethod 
In class method by default first argument is cls
cls always pointing to class
if we not mention @classmethod it act like a instance method.
In class method object creation in not mandatory
"""
class Demo:
    @classmethod
    def class_method(cls):
        print("class method")
        print(cls)  # show main class
Demo.class_method()

# Accessing class variable
class School:
    school_name="ABC public school"     # class variable
    @classmethod
    def display(cls):
        print("school name is",cls.school_name)
School.display()

# modified class variable by using class name
class RLT:
    exam_date="23-01-2026"
    @classmethod
    def collage1(cls):
        print("waiting for exam")
        print(f"exam data is {cls.exam_date}")
    @classmethod
    def collage2(cls):
        print("waiting for exam")
        print(f"exam date is {cls.exam_date}")
RLT.collage1()
RLT.collage2()
RLT.exam_date="20-01-2026"
RLT.collage1()
RLT.collage2()