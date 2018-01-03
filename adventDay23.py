import time
def problem1(path):
	varDict = {}
	insList = readFile(path)

	i = 0
	mul = 0
	while(i < len(insList)):
		insTuple = insList[i].split(" ")
		if insTuple[1] in varDict:
			xVal = varDict[insTuple[1]]
		else:
			xVal = 0
			varDict[insTuple[1]] = xVal

		if len(insTuple) == 3:
			if is_digit(insTuple[2]):
				yVal = int(insTuple[2])
			else:
				yVal = varDict[insTuple[2]]

		ins = insTuple[0]

		if ins == "set":
			varDict[insTuple[1]] = yVal
	 
		elif ins == "add":
			varDict[insTuple[1]] = xVal + yVal

		elif ins == "sub":
			varDict[insTuple[1]] = xVal - yVal

		elif ins == "mul":
			varDict[insTuple[1]] = xVal * yVal
			mul += 1			

		elif ins == "jnz":
			if xVal != 0:
				i += yVal - 1
		i += 1

	print(mul)
			

def is_digit(num):
	try:
		int(num)
		return True
	except Exception:
		return False

def readFile(path):
	with open(path, "r") as f:
		temp = f.read().splitlines()
	return temp

problem1("adventDay23.txt")