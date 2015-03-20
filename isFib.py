#basic variables
x = 0
place = 1

#Gets the length of the squence that needs to be generated ,T, and generates the Fibonnaci numbers up to that point
def fibCreate(T):
    counter = 0
    fibSquence = [0, 1]
    fib1 = 0
    fib2 = 1

    while counter < T:
        fib3 = fib2 + fib1
        fib1 = fib2
        fib2 = fib3

        fibSquence.append(fib2)
        counter += 1

    return fibSquence


#Takes the entry number N and checks if its in the squence, greater then the generated squence, or is not in the squence 
#and returns the apporiate number for each

def CheckFib(N):
    if N > fibSquence[len(fibSquence) - 2]:
        return 0
    for num in fibSquence:
        if N == num:
            return 1
    return 2

#The first input is to find out the number of entries there will be
entry = input()
fibSquence = fibCreate(20)

#This while loop block loops until all the entries are filtered into IsFibo or IsNotFibo
while x < int(entry):
    entryNumber = int(input())
    checkFib = CheckFib(entryNumber)

    while checkFib == 0:
        place += 1
        fibSquence = fibCreate(place * 20) #Expands the lenght of the generated Fib squence
        checkFib = CheckFib(entryNumber)

    if checkFib == 1:
        print("IsFibo")
    elif checkFib == 2:
        print("IsNotFibo")
    x += 1
