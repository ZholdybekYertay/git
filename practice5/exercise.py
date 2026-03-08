#1
import re
s = input()
if re.fullmatch(r"ab*", s):
    print("Match")
else:
    print("No match")
    

#2
import re
s = input()
if re.fullmatch(r"ab{2,3}", s):
    print("Match")
else:
    print("No match")
    
#3
import re
s = input()
print(re.findall(r"[a-z]+_[a-z]+", s))

#4
import re
s = input()
print(re.findall(r"[A-Z][a-z]+", s))

#5
import re
s = input()
if re.search(r"a.*b", s):
    print("Match")
else:
    print("No match")
    
#6
import re
s = input()
result = re.sub(r"[ ,.]", ":", s)
print(result)

#7
s = input()
parts = s.split("_")
camel = parts[0]
for word in parts[1:]:
    camel += word.capitalize()
print(camel)

#8
import re
s = input()
parts = re.findall(r"[A-Z][a-z]*", s)
print(parts)

#9
import re
s = input()
result = re.sub(r"([A-Z])", r" \1", s)
print(result.strip())


#10
import re
s = input()
result = re.sub(r"([A-Z])", r"_\1", s).lower()
print(result.lstrip("_"))
