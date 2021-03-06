def problem1(path):
	lines = readFile(path)
	parents = []
	children = []
	
	for line in lines:
		
		if line.find(" -> ") != -1:
			parents.append(line[0:line.index(" (")])
			foundI = line.index(" -> ")
			children += line[foundI+4:len(line)].split(", ")
			
	print(findBase(parents, children))



def findBase(parents, children):
	for parent in parents:
		if parent not in children:
			return parent

	return "Base not found"

def problem2(path):
	lines = readFile(path)
	parents = []
	children = []
	weights = {}
	
	for line in lines:
		weights[line[0:line.index(" (")]] = line[line.index("(")+1:line.index(")")]
		if line.find(" -> ") != -1:
			parents.append(line[0:line.index(" (")])
			foundI = line.index(" -> ")
			children += line[foundI+4:len(line)].split(", ")

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

problem1("sample.txt")