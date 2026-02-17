# 1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade


# 2
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof")


# 3
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")


# 4
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand)
        self.year = year
