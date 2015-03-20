x = 0
finalNumber = []
length = int(input())

while x < length:
	numbers = input().split()
	if numbers[0] < numbers[1]:
		finalNumber.append(numbers[0])
	elif numbers[0] > numbers[1]:
		finalNumber.append(numbers[1])
	x +=1
	numbers[:] = []

for i in finalNumber:
	print(i, end=" ")