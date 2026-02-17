# 1
class A:
    def method_a(self):
        print("A")

class B:
    def method_b(self):
        print("B")

class C(A, B):
    pass


# 2
class Father:
    def skills(self):
        print("Driving")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass


# 3
class Writer:
    def write(self):
        print("Writing")

class Speaker:
    def speak(self):
        print("Speaking")

class Person(Writer, Speaker):
    pass


# 4
class X:
    def show(self):
        print("X")

class Y:
    def show(self):
        print("Y")

class Z(X, Y):
    pass
