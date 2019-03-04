from math import pow
twoMillion = 2 * pow(10,6)
print (str(twoMillion))

def isPrime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i +2) == 0:
            return False
        i += 6
    return True

def sumOfPrimesToLimit(limit):
    if limit <2:
        return 0
    if limit ==2:
        return 2
    sumOfPrimes = 2
    num = 3
    while num < limit :
        if isPrime(num):
            sumOfPrimes += num
        num +=2
    return sumOfPrimes

print("Sum below 10 is 17")
print(str(sumOfPrimesToLimit(10)))
print(str(sumOfPrimesToLimit(twoMillion)))