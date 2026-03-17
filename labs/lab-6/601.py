n = int(input())
s = 0
b = map(int, input().split())
for i in b:
    s += i * i
print(s)