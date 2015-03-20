x = 0


def findDigits(number):
    numFactors = 0
    intNumber = int(number)
    for digit in number:
        digit = int(digit)
        if digit != 0:
            if intNumber % digit == 0:
                numFactors += 1
    return numFactors


testCases = int(input())
while x < testCases:
    number = input()
    totalFactors =  findDigits(number)
    print(totalFactors)
    x += 1