def genf(n):
    global a , b
    a = 0
    b = 1
    for i in range(n):
        yield a
        a , b = b , a + b
n = int(input())
s = -1
for i in genf(n):
    s += 1
    if s + 1 < n:
        print(i , end = ",")
    elif s == n - 1:
        print(i)