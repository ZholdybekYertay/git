n = int(input())
b = map(int, input().split())
v = all(i >= 0 for i in b)
if v:
    print("Yes")
else:
    print("No")