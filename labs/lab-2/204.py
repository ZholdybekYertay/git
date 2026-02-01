n = int(input())
s = 0
b = map(int, input().split())
for i in b:
    if i > 0:
        s += 1
print(s)