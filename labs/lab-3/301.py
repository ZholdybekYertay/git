def isValid(a):
    n = 0
    s = str(a)
    for i in s:
        if int(i) % 2 != 0:
            print("Not valid")
            break
        else:
            n += 1        
    if len(s) == n:
        print("Valid")
a = int(input())
(isValid(a))