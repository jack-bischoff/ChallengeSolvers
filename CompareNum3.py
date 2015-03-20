x = 0
inputLen = int(input())
minNums = []

while x < inputLen:
	numList = input().split()
	minNums.append(min(map(int,numList)))
	x += 1

for i in minNums:
	print(int(i), end = " ")