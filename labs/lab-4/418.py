import math

line1 = input().split()
x1 = float(line1[0])
y1 = float(line1[1])

line2 = input().split()
x2 = float(line2[0])
y2 = float(line2[1])

reflect_x = (x1 * y2 + x2 * y1) / (y1 + y2)
reflect_y = 0.0

print(f"{reflect_x:.10f} {reflect_y:.10f}")