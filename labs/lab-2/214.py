n = int(input())
a = list(map(int, input().split()))

m = 0
an = a[0]

for i in range(n):
    c = 0
    for j in range(n):
        if a[i] == a[j]:
            c += 1

    if c > m or (c == m and a[i] < an):
        m = c
        an = a[i]

print(an)
