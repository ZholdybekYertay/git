n = int(input())
b = list(map(int, input().split()))

for i in range(n):
    newbie = True
    for j in range(i):
        if b[i] == b[j]:
            newbie = False
            break
    if newbie:
        print("YES")
    else:
        print("NO")
