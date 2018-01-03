insList = [] #lista instrucciones
valDict = {} #llave variable, val (valor actual, ult valor rep)

def problem1(path):
	lines = readFile(path)
	for line in lines:
		spLine = line.split(" ")
		if len(spLine) == 3:
			insList.append((spLine[0], spLine[1], spLine[2]))
		else:
			insList.append((spLine[0], spLine[1], ""))
	
	followInstruction(0)
		



def followInstruction(currI):
	insTuple = insList[currI]
	ins = insTuple[0] #insList -> 0 instruccion 1 x 2 y

	if insTuple[1] in valDict:
		currX = valDict[insTuple[1]][0]
	else:
		valDict[insTuple[1]] = (0, -1)
		currX = 0
	
	if insTuple[2] != "":
		if insTuple[2].isdigit():
			currY = int(insTuple[2])
		else:
			currY = valDict[insTuple[2]][0]

	if ins is "snd":
		valDict[insTuple[1]][1] = currX 

	elif ins is "set":
		valDict[insTuple[1]][0] = currY
 
	elif ins is "add":
		valDict[insTuple[1]][0] = currX + currY

	elif ins is "mul":
		valDict[insTuple[1]][0] = currX * currY

	elif ins is "mod":
		valDict[insTuple[1]][0] = currX % currY

	elif ins is "rcv":
		if currX != 0:
			print(valDict[insTuple[1]][1])
			return
	elif ins is "jgz":
		if currX > 0:
			currI += currY
			followInstruction(currI)

	followInstruction(currI + 1)




def swapVal(x, newVal, valDict):
	aux = valDict[x][1]
	valDict[x][0] = aux
	valDict[x][1] = newVal

def readFile(path):
	with open(path, "r") as f:
		temp = f.read().splitlines()
	return temp	

problem1("inputDay18.txt")