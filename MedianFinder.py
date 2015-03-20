x = 0
medians = []

def  findMedian(numList):
#operations occur here
	maxNum = max(numList)
	minNum = min(numList)
	for number in numList:
		if number != maxNum:
			if number != minNum:
				median = number
				return median


length = int(input())
while x < length:
	nums = input().split()
	numList = list(map(int, nums))
	medians.append(findMedian(numList))
	x += 1

for i in medians:
	print(i, end= ' ' )