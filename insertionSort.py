
def insertionSort(ar):
	lenAr = len(ar)-1
	unSorted = ar[lenAr]
	for index in range(1, lenAr+1):
		activeCell = lenAr - index
		activeValue = ar[activeCell]
		if unSorted < activeValue:
			ar[activeCell + 1] = activeValue
		elif unSorted > activeValue:
			ar[activeCell + 1] = unSorted
		for i in ar:
			print(int(i), end=" ")



lenList = int(input())
sortedList = input().split()
sortedList = list(map(int, sortedList))
insertionSort(sortedList)
