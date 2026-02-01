n = int(input())
s = 0.5
for i in range(n):
    if s * 2 > n:
        break
    else:
        print(int(s * 2) , end=" ")
    s *= 2
