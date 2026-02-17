
n = int(input())
arr = list(map(int, input().split()))
q = int(input())

operation = []

for i in range(q):
    p = input().split()
    
    if p[0] == "add":
        x = int(p[1])
        operation.append(lambda a, x = x: a + x)
        
    elif p[0] == "multiply":
        x = int(p[1])
        operation.append(lambda a, x = x: a * x)
        
    elif p[0] == "power":
        x = int(p[1])
        operation.append(lambda a, x = x: a ** x)
        
    elif p[0] == "abs":
        operation.append(lambda a: abs(a))

for i in operation:
    arr = list(map(i, arr))

print(*arr)
