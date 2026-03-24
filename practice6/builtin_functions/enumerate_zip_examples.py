from functools import reduce
nums = list(map(int, input().split()))
squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
total = reduce(lambda x, y: x + y, nums)
print(f"Squared: {squared}\nEvens: {evens}\nTotal: {total}")