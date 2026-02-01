n , l ,r = map(int, input().split())
b = list(map(int, input().split()))
for i in range(l-1):
    print(b[i], end=" ")
for j in range(r - 1 , l - 2 , -1):
    print(b[j], end=" ")
for i in range(r, n):
    print(b[i], end=" ")