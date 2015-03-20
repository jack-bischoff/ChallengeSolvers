constMultiplier = 5/9
convertedTemp = []
temperatures = []

def Conversion(temp):
    raw_fahrenheit = (temp - 32)* constMultiplier
    return round(raw_fahrenheit)


tempList = input().split()
tempLen = int(tempList[0])
del tempList[0]

for temp in tempList:
    temperatures.append(int(temp))

for temperature in temperatures:
    convertedTemp.append(Conversion(temperature))

for i in convertedTemp:
    print(i, end=" ")