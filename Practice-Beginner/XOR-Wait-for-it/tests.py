
#To be moved to xor.py sometime

def getInTestNumber():
    t = input("Number of Tests?")
    if str.isdigit(t):
        return int(t)
    else:
        return 0
def getInL():
    t = input("L?")
    if str.isdigit(t):
        return int(t)
    else:
        return 0
def getInR():
    t = input("R?")
    if str.isdigit(t):
        return int(t)
    else:
        return 0
def getInXPairs(numberOfPairs):
    count = 0
    while numberOfPairs != 0:
        l = getInL()
        r = getInR()
        numberOfPairs -= 1
        count += 1
    return count

#testsuite
def getInTestNumberNotNone():
    t = getInTestNumber()
    return t != None
def getInTestNumberIsNumber():
    t = getInTestNumber()
    return type(t) == type(0)
def getsInXPairsOfTests(numberOfPairs):
    initialNumber = numberOfPairs
    count = 0
    while numberOfPairs != 0:
        l = getInL()
        r = getInR()
        numberOfPairs -= 1
        count += 1
    print(str(count))
    print(str(initialNumber))
    return count == initialNumber



def runTests():
    print("Running Tests... ")
    print("getInTestNumberNotNone()....." + str(getInTestNumberNotNone()))
    print("getInTestNumberIsNumber()...." + str(getInTestNumberIsNumber()))
    print("getsInXPairsOfTests(2)...." + str(getsInXPairsOfTests(2)))
    print("Done Running Tests... ")




runTests()