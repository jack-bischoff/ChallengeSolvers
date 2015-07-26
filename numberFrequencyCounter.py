data = input().split()
numLimit = int(data[1])
nums = input().split()
nums = list(map(int, nums))
counterArray = [0] * numLimit

for number in nums:
    counterArray[number - 1] += 1


for i in counterArray:
    print(i, end=" ")
