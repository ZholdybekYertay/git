names = list(map(str, input().split()))
scores = list(map(int, input().split()))
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")
    

for name, score in zip(names, scores):
    print(f"{name} scored {score}")


val = input()
if isinstance(val, str):
    num = int(val)
    print(f"Converted {type(val)} to {type(num)}")