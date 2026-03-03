def genf(n):
    for i in range(n + 1):
        yield 2 ** i

n = int(input())
for i in genf(n):
    print(i , end = " ")
