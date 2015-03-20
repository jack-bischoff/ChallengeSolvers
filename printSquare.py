def genSquare(coords):
	x = coords[0]
	y = coords[1]
	for i in range(0,y):
		print("*"*x,end="\n")


coords = input("Enter (x,y) coords: ").split()
coords = list(map(int, coords))
genSquare(coords)