n = int(input())
b = map(int, input().split())
v = list(filter(lambda x : x % 2 == 0 , b))
print(len(v))