#1
import math
n = int(input())
p = math.pi
r = n * p / 180
print(f"{r:.6f}")

#2
h = float(input())
b1 = float(input())
b2 = float(input())
s = ((b1 + b2) / 2) * h
print(s)

#3
import math
n = int(input())
s = float(input())
area = (n * s**2) / (4 * math.tan(math.pi / n))
print(area)

#4
b , h = map(float, input().split())
print( b * h)