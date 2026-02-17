# 1
class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    def speak(self):
        print("Woof")


# 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return 4


# 3
class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def greet(self):
        print("Hi, I'm a student")


# 4
class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        print("Cannot fly")
