import sys
def problem1(path):
	lines = readFile(path)
	row = ""
	maxNum = -sys.maxsize - 1
	minNum = sys.maxsize
	checkSum = 0
	for i in range(len(lines)):
		row = lines[i].split("	")
		for j in range(len(row)):
			if int(row[j]) > maxNum:
				maxNum = int(row[j])
			if int(row[j]) < minNum:
				minNum = int(row[j])
		checkSum += (maxNum - minNum)
		maxNum = -sys.maxsize - 1
		minNum = sys.maxsize

	print(checkSum)

def problem2(path):
	lines = readFile(path)
	row = ""
	div = 0.0
	checkSum = 0
	for i in range(len(lines)):
		row = lines[i].split("	")
		for j in range(len(row)):
			for k in range(len(row)):
				if k!=j and (float(row[j]) % float(row[k]) == 0):
					div = float(row[j]) / float(row[k])
					break
			if div!= 0:
				checkSum += div
				div = 0
				break

	print(checkSum)


def readFile(path):
	with open(path, "r") as f:
		temp = f.read().splitlines()
	return temp

problem2("input.txt")