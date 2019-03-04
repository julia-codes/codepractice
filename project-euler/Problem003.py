
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

def XdividesByY(x,y):
    return (x % y) == 0

def XdividesByYAndYPrime(x,y):
    if XdividesByY(x,y):
        print(str(y))
        return isPrime(y)
    return False

def nextFactor(x,y):
    print("y is " + str(y))
    while y < brakeLimit:
        y += 1
        if XdividesByY(x,y):
            return y
    return -1

def nextNumToCheck(x, currentLow):
    return x / currentLow

def largestPrime(x):
    currentLow = 2
    num = nextNumToCheck(x, currentLow)
    while num > 2:
        if XdividesByYAndYPrime(x,num):
            return num
        currentLow = nextFactor(x,currentLow)
        num = nextNumToCheck(x, currentLow)
        print("Checking: " + str(currentLow) + " to " + str(num))
    return 1

print("The prime factors of 13195 are 5, 7, 13 and 29.")
largestPrime(13195)

print("The largest prime factor of 600851475143")
largestPrime(600851475143)