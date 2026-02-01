n = int(input())
s = -1e9
j = 0
b = map(int, input(). split())
for i in b:
    j += 1
    if i > s:
        s = i
        m = j
print(m)