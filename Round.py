x = 0
answers = []

inputLength = int(input())

while x < inputLength:
	numbers= list(map(int, input().split()))
	answers.append(round(numbers[0]/numbers[1]))

for i in answers:
	print(i, end = " ")