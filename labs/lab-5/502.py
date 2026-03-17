import re
s = input()
p1 = input()
if re.search(p1 , s):
    print("Yes")
else:
    print("No")