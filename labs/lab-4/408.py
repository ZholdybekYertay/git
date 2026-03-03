def genf(n):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    for i in range(n + 1):
        if isPrime(i):
            yield i

n = int(input())
for i in genf(n):
    print(i, end=" ")