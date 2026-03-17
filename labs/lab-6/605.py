s = input().strip()
vowels = "aeiou"
has_vowel = any(char.lower() in vowels for char in s)
if has_vowel:
    print("Yes")
else:
    print("No")