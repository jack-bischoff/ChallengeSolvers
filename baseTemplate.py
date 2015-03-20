numTestCase = int(input())
x = 0

while x < numTestCase:
    revBi = int()
    biNumber = bin(int(input()))[2:]
    for bit in biNumber:
        if bit == 1:
            revBi += 0
        else:
            revBi += 1
    x += 1