import re
text = "My age is 20"
x = re.search(r"\d+", text)
print(x.group())


import re
text = "a1 b2 c3"
x = re.findall(r"\d", text)
print(x)


import re
text = "apple,banana;orange"
x = re.split(r"[,;]", text)
print(x)


import re
text = "I like cats"
x = re.sub("cats", "dogs", text)
print(x)


import re
text = "Age 25"
print(re.findall(r"\d", text))


import re
text = "111 22 3"
print(re.findall(r"\d+", text))


import re
with open("raw.txt") as f:
    data = f.read()
items = re.findall(r"Item: (\w+) Price: (\d+)", data)
for name, price in items:
    print(name, price)