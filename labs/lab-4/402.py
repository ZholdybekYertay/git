def genf(n):
    for i in range(0 , n + 1 , 2):
        yield i
n = int(input())
for i in genf(n):
    if i + 1 < n:
        print(i, end = ",")
    elif i == n or i == n - 1:
        print(i)