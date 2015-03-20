import sys

arguments = sys.argv[2:]
S = 0
for arg in arguments:
	S += int(arg)
print(S)