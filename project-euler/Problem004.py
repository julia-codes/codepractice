from math import pow

def checkPalindrome(digits):
    stringVersion = str(digits)
    if len(stringVersion) < 2:
        return True
    leftIndex = 0
    rightIndex = len(stringVersion) - 1
    while (leftIndex <= rightIndex):
        leftChar = stringVersion[leftIndex]
        rightChar = stringVersion[rightIndex]
        if leftChar != rightChar:
            return False
        leftIndex += 1
        rightIndex -= 1
    return True

def xDigitMax(x):
    return int(pow(10,x) - 1)

def xDigitMin(x):
    return int(pow(10,x - 1))

def productIsPalindrome(x,y):
    return checkPalindrome( x * y)

def returnString(A,B):
    output = "Higest " + str(A * B)
    output += " is " + str(A) + " " + str(B)
    return output

def largestXDigit(x):
    A = xDigitMax(x)
    B = xDigitMax(x)
    C = xDigitMax(x)
    min = xDigitMin(x)
    currentA = 0
    currentB = 0
    while B >= min:
        while A>=min:
            if productIsPalindrome(A,B):
                if (A * B) > (currentA * currentB):
                    currentA = A
                    currentB = B
            A -= 1
        B -=1
        C -=1
        A = C
    return returnString(currentA,currentB)
    



print("Max of 3- " + str(xDigitMax(3)))
print("Min of 3- " + str(xDigitMin(3)))

print("Largest of 2 Digits should be 9009")
print(largestXDigit(2))

print("Largest of 3 Digits should be ??")
print(largestXDigit(3))