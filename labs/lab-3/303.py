s = input()


to_digit = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}


to_word = {v: k for k, v in to_digit.items()}


for i in range(len(s)):
    if s[i] in "+-*":
        pos = i
        break

op = s[pos]
left_part = s[:pos]
right_part = s[pos+1:]


def decode(string):
    number = ""
    for i in range(0, len(string), 3):
        triplet = string[i:i+3]
        number += to_digit[triplet]
    return int(number)

a = decode(left_part)
b = decode(right_part)


if op == "+":
    result = a + b
elif op == "-":
    result = a - b
else:
    result = a * b


res_str = str(result)
answer = ""

start = 0
if res_str[0] == "-":
    answer += "-"
    start = 1

for digit in res_str[start:]:
    answer += to_word[digit]

print(answer)
