# 1
numbers = [5, 2, 8, 1]
sorted_nums = sorted(numbers, key=lambda x: x)
print(sorted_nums)


# 2
words = ["banana", "apple", "kiwi"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


# 3
students = [("yertay", 90), ("II-yertay", 75), ("III-yertay", 85)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


# 4
names = ["X-Yertay", "V-yertay", "IV-yertay"]
sorted_names = sorted(names, key=lambda x: x.lower())
print(sorted_names)
