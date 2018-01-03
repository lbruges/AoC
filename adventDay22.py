def problem1(path, bursts):
	lines = readFile(path)
	charDict = loadMatrix(lines)
	center = int(len(lines)/2)

	i = center
	j = center
	direct = None
	n = 0

	infect = 0

	while(n < bursts):
		if (i,j) not in charDict:
			charDict[(i,j)] = "."
		
		direct = evalDir(direct, charDict[(i,j)])
		if charDict[(i,j)] == "#":
			charDict[(i,j)] = "."
		else:
			charDict[(i,j)] = "#"
			infect += 1
		if direct  == "N":
			j += 1
		elif direct == "S":
			j -= 1
		elif direct == "E":
			i += 1
		else:
			i -= 1
		n += 1
	print(infect)	
	#res = sum(1 for x in charDict.values() if x == "#")
	#print(res)

def problem2(path, bursts):
	lines = readFile(path)
	charDict = loadMatrix(lines)
	center = int(len(lines)/2)

	i = center
	j = center
	direct = None
	n = 0

	infect = 0
	directList = []
	directList.append(None)
	directList.append(None)

	while(n < bursts):
		if (i,j) not in charDict:
			charDict[(i,j)] = "."
		
		directList = addDirection(direct, directList)		
		
		if charDict [(i,j)] == "F":
			direct = directList[0]
		elif charDict != "W":	
			direct = evalDir(direct, charDict[(i,j)])
		
		if charDict[(i,j)] == ".":
			charDict[(i,j)] = "W"
		elif charDict[(i,j)] == "W":
			charDict[(i,j)] = "#"
			infect += 1
		elif charDict[(i,j)] == "#":
			charDict[(i,j)] = "F"
		else:
			charDict[(i,j)] = "." 
		
		if direct  == "N":
			j += 1
		elif direct == "S":
			j -= 1
		elif direct == "E":
			i += 1
		else:
			i -= 1
		n += 1
	print(infect)	

def addDirection(direct, directList):
	directList.append(direct)
	newList = directList[1:]
	return newList


def loadMatrix(lines):
	charDict = {}
	for i in range(len(lines)):
		line = lines[i]
		for j in range(len(line)):
			charDict[(j, i)] = line[j]

	return charDict


def evalDir(direct, currChar):
	if direct == None:
		if currChar == "#":
			direct = "E"
		else:
			direct = "W"
	elif direct == "E":
		if currChar == "#":
			direct = "N"
		else:
			direct = "S"
	elif direct == "N":
		if currChar == "#":
			direct = "W"
		else:
			direct = "E"
	elif direct == "W":
		if currChar == "#":
			direct = "S"
		else:
			direct = "N"
	elif direct == "S":
		if currChar == "#":
			direct = "E"
		else:
			direct = "W"
	return direct

def readFile(path):
	with open(path, "r") as f:
		temp = f.read().splitlines()
	return temp	

n = input()
problem2("testAdv22.txt", int(n))