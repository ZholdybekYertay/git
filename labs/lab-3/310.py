class Person:
    def __init__(self, name , gpa):
        self.name = name
        self.gpa = gpa
class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name, gpa)
    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")
    
name , gpa = input().split()
student = Student(name , gpa)
student.display()
