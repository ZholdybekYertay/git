n = int(input())
s = -1e9
b = map(int, input(). split())
for i in b:
    if i > s:
        s = i
print(s)