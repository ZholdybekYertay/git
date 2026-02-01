n = int(input())
arr = []

for _ in range(n):
    arr.append(input().strip())

first_pos = {}

for i in range(n):
    if arr[i] not in first_pos:
        first_pos[arr[i]] = i + 1  

for s in sorted(first_pos):
    print(s, first_pos[s])
