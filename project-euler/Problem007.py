from math import pow

brakeLimit = 9999999999

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

def nextPrime(n):
    if n == 2:
        return 3
    n += 2
    while isPrime(n) == False:
        n+=2
        if(n>brakeLimit):
            print("Hit the Breaks")
            exit
    return n

def theXthPrime(x):
    if x <=1:
        return 2
    topPrime = 2
    ithPrime = 1
    print("1st is 2")
    while ithPrime < x:
        topPrime = nextPrime(topPrime)
        ithPrime += 1
        print(str(ithPrime) + "th is " + str(topPrime))
    return topPrime

print("next prime is 3")
print(str(nextPrime(2)))

print("First six top is 13")
print(str(theXthPrime(6)))

print("First 10001 top is ??")
print(str(theXthPrime(10001)))