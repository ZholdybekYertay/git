with open("data.txt", "r") as f:
    print("READ():")
    print(f.read())

with open("data.txt", "r") as f:
    print("\nREADLINE():")
    print(f.readline())

with open("data.txt", "r") as f:
    print("\nREADLINES():")
    print(f.readlines())