import time
def problem1(path):
	bankArr = readFile(path).split("	")
	solutions = []
	solutions.append(';'.join(bankArr))
	res = ''

	currBank = list(map(int, bankArr))
	iteration = 0
	while True:
		maxBank = findMax(currBank)
		if currBank[maxBank] <= (len(currBank) - 1):
			lowerLimit = 0
		else:
			lowerLimit = 1

		i = evaluateLimit(currBank, maxBank)

		while currBank[maxBank] > lowerLimit:
			currBank[i] += 1
			currBank[maxBank] -= 1
			i = evaluateLimit(currBank, i)

		iteration += 1
		res = ';'.join(list(map(str, currBank)))
		
		if res in solutions:
			break
		else:
			solutions.append(res)
	
	print(iteration)

def problem2(path):
	target = '1;1;0;15;14;13;12;10;10;9;8;7;6;4;3;5'

	bankArr = readFile(path).split("	")
	solutions = []
	solutions.append(';'.join(bankArr))
	res = ''

	currBank = list(map(int, bankArr))
	iteration = 0

	flag = False

	while True:
		maxBank = findMax(currBank)
		if currBank[maxBank] <= (len(currBank) - 1):
			lowerLimit = 0
		else:
			lowerLimit = 1

		i = evaluateLimit(currBank, maxBank)

		while currBank[maxBank] > lowerLimit:
			currBank[i] += 1
			currBank[maxBank] -= 1
			i = evaluateLimit(currBank, i)

		
		res = ';'.join(list(map(str, currBank)))
		
		if res in solutions:
			break
		else:
			if res == target:
				flag = True
			solutions.append(res)

		if flag:
			iteration += 1
	
	print(iteration)


		


def findMax(currBank):
	maxNum = -1
	maxIndex = -1
	for i in range(len(currBank)):
		if maxNum == currBank[i]:
			continue
		elif currBank[i] > maxNum:
			maxNum = currBank[i]
			maxIndex = i
	return maxIndex

def evaluateLimit(bankArr, currIndex):
	if currIndex < (len(bankArr) - 1):
		i = currIndex + 1
	else:
		i = 0
	return i

def readFile(path):
	with open(path, "r") as f:
		temp = f.read()
	return temp	

problem2("adventDay6.txt")