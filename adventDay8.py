import sys
def problem1(path):
	lines = readFile(path)
	varDict = {}
	
	for line in lines:
		operation = line[:line.index(" if")]
		condition = line[line.index("if"):]
		opTuple = operation.split(" ")
		cnTuple = condition.split(" ")
		cndIns = cnTuple[0] + " varDict.get('"+cnTuple[1]+"', 0) " + cnTuple[2]+" "+cnTuple[3] + ":\n\t"
		if opTuple[1] == "inc":
			oper = "+"
		elif opTuple[1] == "dec":
			oper = "-"
		if opTuple[0] not in varDict:
			varDict[opTuple[0]] = 0

		opIns = "varDict[opTuple[0]] " + oper + "= "+opTuple[2]
		exec(cndIns+opIns)
		
	print(max(varDict.values()))


def problem2(path):
	lines = readFile(path)
	varDict = {}
	maxVal = -(sys.maxsize)

	for line in lines:
		operation = line[:line.index(" if")]
		condition = line[line.index("if"):]
		opTuple = operation.split(" ")
		cnTuple = condition.split(" ")
		cndIns = cnTuple[0] + " varDict.get('"+cnTuple[1]+"', 0) " + cnTuple[2]+" "+cnTuple[3] + ":\n\t"
		if opTuple[1] == "inc":
			oper = "+"
		elif opTuple[1] == "dec":
			oper = "-"
		if opTuple[0] not in varDict:
			varDict[opTuple[0]] = 0

		opIns = "varDict[opTuple[0]] " + oper + "= "+opTuple[2]
		exec(cndIns+opIns)
		if varDict[opTuple[0]] > maxVal:
			maxVal = varDict[opTuple[0]]
		
	print(maxVal)


def readFile(path):
	with open(path, "r") as f:
		temp = f.read().splitlines()
	return temp

problem2("adventDay8.txt")