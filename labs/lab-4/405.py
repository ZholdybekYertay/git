def genf(n):
    for i in range(n , -1 , -1):
        yield i
n = int(input())
for i in genf(n):
    print(i)