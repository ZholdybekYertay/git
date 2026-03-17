import re
s = input()
def double_digit(m):
    digit = m.group(0) 
    return digit * 2   
result = re.sub(r"\d", double_digit, s)
print(result)