# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('welcome to project sections ')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import datetime

class Student:
    # CLASS VARIABLE: Shared by all students (The "University Brand")
    university_name = "Global Tech University"
    total_students = 0

    # 1. THE CONSTRUCTOR: Initializes a unique student
    # Used when a student first enrolls.
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.courses = []
        # Updates the shared class state every time a new student is born
        Student.total_students += 1
        print(f"Enrollment successful: Welcome {self.name}!")

    # 2. INSTANCE METHOD: Acts on a specific student's data
    # Used when a specific student wants to join a course.
    def enroll_in_course(self, course_name: str):
        self.courses.append(course_name)
        print(f"{self.name} is now enrolled in: {course_name}")

    # 3. CLASS METHOD: Acts on the whole University (the Class)
    # Used for "Factory" creation or changing university-wide rules.
    @classmethod
    def change_university_name(cls, new_name: str):
        cls.university_name = new_name
        print(f"University rebranded to: {cls.university_name}")

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):
        # Factory Method: Creates a Student object using different logic
        email = f"{name.lower()}@gtu.edu"
        return cls(name, email)

    # 4. STATIC METHOD: A general utility tool
    # Does not need student data or university data.
    # Just a helper that belongs logically in this class.
    @staticmethod
    def is_work_day(date_obj):
        # Simple utility to check if the university is open
        return date_obj.weekday() < 5  # Mon-Fri are work days

# --- Execution in the Real World ---

# [CONSTRUCTOR] runs here
student1 = Student("Alice", "alice@email.com")

# [INSTANCE METHOD] used to change Alice's specific state
student1.enroll_in_course("Python for AI")

# [CLASS METHOD] used as a "Factory" to create a student differently
student2 = Student.from_birth_year("Bob", 2005)

# [CLASS METHOD] used to update ALL students at once
Student.change_university_name("Future Tech Academy")
print(f"Alice's school is now: {student1.university_name}")

# [STATIC METHOD] used as a tool (independent of any specific student)
today = datetime.date.today()
if Student.is_work_day(today):
    print("The University is currently open for admissions.")
