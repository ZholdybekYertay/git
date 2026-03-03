#1
def genf(n):
    for i in range(n):
        yield i * i
n = int(input())
for i in genf(n):
    print(i, end = " ")
    
#2
def genf(n):
    for i in range(n):
        if i % 2 == 0:
            yield i
n = int(input())
s = 0
if n % 2 == 1: 
    for i in genf(n):
        if s + 1 < n // 2 + 1:
            print(i , end=",")
        elif s == n // 2:
            print(i)
        s += 1
else:
    for i in genf(n):
        if s + 1 < n // 2:
            print(i , end=",")
        elif s == n // 2 - 1:
            print(i)
        s += 1

#3
n = int(input())
x = (i for i in range(n + 1) if i % 12 == 0)
for i in x:
    print(i, end = " ")

#4
def squares(a , b):
    for i in range(a , b + 1):
        yield i ** 2
a , b = map(int , input().split())
for i in squares(a , b):
    print(i , end = " ")

#5
n = int(input())
x = (i - 1 for i in range(n + 1 , -1 , -1))
while n > 0:
    print(next(x), end= " ")
    n -= 1
