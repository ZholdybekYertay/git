n = int(input())
x = (i ** 2 for i in range(1, n + 1))
while n > 0:
    print(next(x))
    n -= 1