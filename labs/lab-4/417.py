import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

segment_len = math.hypot(dx, dy)

a = dx * dx + dy * dy
b = 2 * (x1 * dx + y1 * dy)
c = x1 * x1 + y1 * y1 - R * R

D = b * b - 4 * a * c

def inside(x, y):
    return x*x + y*y <= R*R + 1e-12

if D < 0:
    if inside(x1, y1) and inside(x2, y2):
        ans = segment_len
    else:
        ans = 0.0
else:
    sqrtD = math.sqrt(max(0.0, D))

    t1 = (-b - sqrtD) / (2 * a)
    t2 = (-b + sqrtD) / (2 * a)

    if t1 > t2:
        t1, t2 = t2, t1

    left = max(0.0, t1)
    right = min(1.0, t2)

    if left > right:
        if inside(x1, y1) and inside(x2, y2):
            ans = segment_len
        else:
            ans = 0.0
    else:
        ans = (right - left) * segment_len

print(f"{ans:.10f}")