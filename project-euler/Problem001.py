print("Problem 1")

def getLimit():
    t = input("Number to check to?")
    return t

def XdivisibleByY(x,y):
    return (x % y) == 0

def divisibleBy3or5(x):
    dividesBy3 = XdivisibleByY(x,3)
    dividesBy5 = XdivisibleByY(x,5)
    return dividesBy3 or dividesBy5

def sumBelowDividingBy3or5(x):
    num = 1
    result = 0
    while num < x:
        if (divisibleBy3or5(num)):
            result += num
        num += 1
    return result

def getSumDivisibleBy3or5():
    return sumBelowDividingBy3or5(getLimit())

print(str(getSumDivisibleBy3or5()))
