# 1
def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Zholdybek")


# 2
def power(base, exponent=2):
    print(base ** exponent)

power(3)
power(3, 3)


# 3
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old")

introduce(age=18, name="Yertay")


# 4
def multiply(a, b=1):
    print(a * b)

multiply(5)
multiply(5, 4)
