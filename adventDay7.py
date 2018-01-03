def problem1(path):
	lines = readFile(path)
	parents = []
	children = []
	#parentCodes = {}
	for line in lines:
		if line.find(" -> ") != -1:
			#parentCodes[line[0:line.index(" (")]] = int(line[line.index("(")+1:line.index(")")])
			foundI = line.index(" -> ")
			parents.append(line[0:line.index(" (")])
			children.append(line[foundI+4:len(line)].split(", "))
			#parents[line[0:line.index(" (")]] = line[foundI+4:len(line)].split(", ")

	print(findBase(parents, children))


def findBase(parents, children):
	for i in range(len(parents)):
		tempParent = parents[i] 
		parentIndex = i
		found = False
		for j in range(len(children)):
			if j != parentIndex:
				if tempParent in children[j]:
					found = True
					break
		if not found:
			return tempParent

	return "Base not found"

def problem2(path):
	lines = readFile(path)
	parents = []
	children = []
	weights = {}
	#parentCodes = {}
	for line in lines:
		weights[line[0:line.index(" (")]] = int(line[line.index("(")+1:line.index(")")])
		if line.find(" -> ") != -1:
			foundI = line.index(" -> ")
			parents.append(line[0:line.index(" (")])
			children.append(line[foundI+4:len(line)].split(", "))
			#parents[line[0:line.index(" (")]] = line[foundI+4:len(line)].split(", ")

	base = findBase(parents, children)
	
	parentWeights = {}

	for i in range(len(parents)):
		if parents[i] != base:
			weight = weights[parents[i]] + sumChildren(children[i], weights)
			if weight not in parentWeights:
				parentWeights[weight] = 1
			else:
				parentWeights[weight] += 1

	print(parentWeights)

def sumChildren(childrenArr, weights):
	totalSum = 0
	for child in childrenArr:
		totalSum += weights[child]

	return totalSum
			


def testFunct(stringTemp):
	foundI = -1
	try:
		foundI = stringTemp.index(" -> ")
	except Exception:
		print(" ->  not in string")
	
	if foundI != -1:
		print(stringTemp[0:foundI])
		print(stringTemp[foundI+4:len(stringTemp)])

	print(stringTemp[stringTemp.index("(")+1:stringTemp.index(")")])


def readFile(path):
	with open(path, "r") as f:
		temp = f.read().splitlines()
	return temp	

problem2("adventDay7.txt")