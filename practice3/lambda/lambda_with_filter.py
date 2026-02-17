# 1
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


# 2
nums = [10, 3, 7, 20]
greater_than_5 = list(filter(lambda x: x > 5, nums))
print(greater_than_5)


# 3
words = ["cat", "elephant", "dog"]
long_words = list(filter(lambda x: len(x) > 3, words))
print(long_words)


# 4
names = ["Yertay", "Yertay-2", "Yertay-33"]
long_names = list(filter(lambda x: len(x) > 4, names))
print(long_names)
