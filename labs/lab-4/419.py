import math

R = float(input())

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

L1 = math.sqrt(x1**2 + y1**2)
L2 = math.sqrt(x2**2 + y2**2)

dist_AB = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

angle_A = math.atan2(y1, x1)
angle_B = math.atan2(y2, x2)
gamma = abs(angle_A - angle_B)
if gamma > math.pi:
    gamma = 2 * math.pi - gamma

alpha = math.acos(R / L1)
beta = math.acos(R / L2)

if gamma > alpha + beta:
    side1 = math.sqrt(max(0, L1**2 - R**2))
    side2 = math.sqrt(max(0, L2**2 - R**2))
    arc_length = R * (gamma - alpha - beta)
    result = side1 + side2 + arc_length
else:
    result = dist_AB

print(f"{result:.10f}")