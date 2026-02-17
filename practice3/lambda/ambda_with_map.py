# 1
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
print(squared)


# 2
names = ["Zholdybek", "Yertay"]
upper = list(map(lambda x: x.upper(), names))
print(upper)


# 3
nums = [5, 10, 15]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)


# 4
words = ["hi", "python"]
lengths = list(map(lambda x: len(x), words))
print(lengths)
