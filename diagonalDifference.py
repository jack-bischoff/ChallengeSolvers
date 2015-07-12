d1Sum = 0
d2Sum = 0
matrix = []

n = int(input())
for i in range(0, n):
    matrix.append(input().split())
    
for index, row in enumerate(matrix):
    d1Sum += int(row[index])
    d2Sum += int(row[(len(matrix) - 1) - index])
    
print(int((((d1Sum - d2Sum)**2)**0.5)))
