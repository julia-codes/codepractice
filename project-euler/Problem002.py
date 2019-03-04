from math import pow
fourMillion = 4 * pow(10,6)
print (str(fourMillion))

def addTwo(x,y):
    return x + y

def isEven(x):
    return (x % 2) == 0

def fibonaciToLimit(limit):
    x = 1
    y = 0
    sumOfEvens = 0
    while x < limit :
        if isEven(x):
            sumOfEvens += x
        nextNum = addTwo(x,y)
        y = x
        x = nextNum
    return sumOfEvens

print("Sum of Evens below 4 Million: " + str(fibonaciToLimit(90)))
print("should be " + str(2 + 8 + 34))
print("Sum of Evens below 4 Million: " + str(fibonaciToLimit(fourMillion)))
