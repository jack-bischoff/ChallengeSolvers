x = 0
#This is the equation which models the growth of the tree
#N = cycles NOTE: this equation works only for odd cycles.
#the even equation is -1 for the constant term
Equation = '2 * ( 2 ** ( (n / 2 ) + 0.5 ) ) - 2'

#Function for calculating the growth
def calGrowth(n=0):
	if n % 2 != 0:
		g = int(eval(Equation))
		return g
	else:
		n  -= 1
		g = int(eval(Equation)) + 1
		return g

numTestCases = int(input())
#Control  Loop
while x < numTestCases:
	cycles = int(input())
	growth = calGrowth(cycles)
	print(growth)
	x +=1
