def genf(b , n):
    for i in range(n):
        for item in b:
            yield item

b = input().split()
n = int(input())
r = genf(b , n)
print(*(r))