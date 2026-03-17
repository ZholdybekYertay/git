import re
text = input()
pattern = r"\d{2}/\d{2}/\d{4}"
matches = re.findall(pattern, text)
print(len(matches))