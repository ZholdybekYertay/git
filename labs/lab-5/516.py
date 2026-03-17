import re
line = input()
match = re.search(r"Name: (.+), Age: (.+)", line)

if match:
    name = match.group(1)
    age = match.group(2)
    print(f"{name} {age}")