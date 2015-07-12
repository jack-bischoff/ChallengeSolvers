posNum, negNum, zNum = 0,0,0


n = int(input())
numbers = input().split()
numbers = list(map(int, numbers))

for num in numbers:
    if num > 0:
        posNum += 1
    elif num < 0:
        negNum += 1
    else:
        zNum += 1

print(posNum/n)
print(negNum/n)
print(zNum/n)