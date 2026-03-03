def genf(n):
    for i in range(n+1):
        if i % 12 == 0:
            yield i
            
n = int(input())
for i in genf(n):
    print(i, end = " ")