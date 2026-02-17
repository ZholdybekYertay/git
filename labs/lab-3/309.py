class Circle:
    def __init__(self , radius):
        self.radius = radius
    def area(self):
        return r * r * 3.14159
        
r = int(input())
circle = Circle(r)
ansss = circle.area()
print(f"{ansss:.2f}")