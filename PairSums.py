x = 0
finalSum = []
length = int(input())

while x < length:
	numbers = input().split()
	finalSum.append(int(numbers[0]) + int(numbers[1]))
	x +=1

for i in finalSum:
	print(i, end=" ")