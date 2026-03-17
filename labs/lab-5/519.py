import re
text = input()
word_pattern = re.compile(r"\b\w+\b")
words = word_pattern.findall(text)
print(len(words))