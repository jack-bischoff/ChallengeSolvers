x = 0
finalBMIGrades = []
BMIGrades = ["under","normal","over","obese"]

def CalculateBMI(personData):
		BMI = personData[0]/(personData[1]**2)
		if BMI >= 30.0:
			return BMIGrades[3]
		elif BMI >= 25.0:
			if BMI < 30.0:
				return BMIGrades[2]
		elif BMI >= 18.5:
			if BMI < 25.0:
				return BMIGrades[1]
		elif BMI < 18.5:
			return BMIGrades[0]


numPeople = int(input())
while x < numPeople:
	numList = input().split()
	personData = list(map(float, numList))
	finalBMIGrades.append(CalculateBMI(personData))
	x += 1


#for printing the final result
for i in finalBMIGrades:
	print(i, end= " ")