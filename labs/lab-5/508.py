import re
s = input()
pattern = input()
print(",".join(re.split(pattern, s)))