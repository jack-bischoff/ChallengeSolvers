x = 0
vowelCountList = []
vowels = "aeiouy"


def searchVowels(word):
	# operations occur here
	vowelCount = 0
	for letter in word:
		if letter in vowels:
			vowelCount += 1
	return vowelCount


length = int(input())
while x < length:
	word = input()
	vowelCountList.append(searchVowels(word))
	x += 1
# for printing the final result
for i in vowelCountList:
	print(i, end= " ")