import math

def problem1(num):
	upperRoot = math.ceil(math.sqrt(num))
	upperLimit = math.pow(upperRoot,2)
	diag = upperLimit - (upperRoot - 1)
	
	if num <= upperLimit and num >= diag:
		if upperRoot%2 == 0:
			sideDist = num - (upperLimit - (int(upperRoot/2) - 1))
		else: 
			sideDist = num - (upperLimit - int(upperRoot/2))
	else:
		sideDist = num - (diag - int(upperRoot/2))

	distToCenter = int(upperRoot/2)

	print(abs(sideDist) + abs(distToCenter))

def problem2(n):
	lenx = n
	leny = n

	Matrix = [[0 for x in range(lenx)] for y in range(leny)]
	
	base_i = int(lenx/2) - 1
	base_j = int(leny/2) - 1
	Matrix[base_i][base_j] = 1
	step = 0
	aux = 0
	i = base_i
	j = base_j

	while (i >= 0 and i < lenx) or (j >= 0 and j < leny) : 
		
		print("-------------")
		print("Step"+str(step))
		print("aux "+ str(aux))
		print("i "+ str(i))
		print("j "+ str(j))
		print("-------------")  

		if isValid(j+1, leny) and isValid(i, lenx) and isValid(j, leny):
			Matrix[i][j] += Matrix[i][j+1]
		if isValid(i+1, lenx) and isValid(j, leny) and isValid(i, lenx):
			Matrix[i][j] += Matrix[i+1][j]
		if isValid(i+1, lenx) and isValid(j+1, leny) and isValid(i, lenx) and isValid(j, leny):
			Matrix[i][j] += Matrix[i+1][j+1]
		if isValid(j-1, leny) and isValid(i, lenx) and isValid(j, leny):
			Matrix[i][j] += Matrix[i][j-1]
		if isValid(i-1, lenx) and isValid(j, leny) and isValid(i, lenx):
			Matrix[i][j] += Matrix[i-1][j]
		if isValid(i-1, lenx) and isValid(j-1, leny) and isValid(i, lenx) and isValid(j, leny):
			Matrix[i][j] += Matrix[i-1][j-1]
		if isValid(i-1, lenx) and isValid(j+1, leny) and isValid(i, lenx) and isValid(j, leny):
			Matrix[i][j] += Matrix[i-1][j+1]
		if isValid(i+1, lenx) and isValid(j-1, leny) and isValid(i, lenx) and isValid(j, leny):
			Matrix[i][j] += Matrix[i+1][j-1]

		if step == 0:
			aux += 1
			i += aux
			step = 1
			continue
		if step == 1:
			if j < (base_j + aux):
				j += 1
			else:
				step = 2
			continue
		if step == 2:
			if i > (base_i - aux):
				i -= 1
			else:
				step = 3
			continue
		if step == 3:
			if j > (base_j - aux):
				j -= 1 
			else:
				step = 4
			continue
		if step == 4:
			if i < (base_i + aux):
				i += 1
			else:
				step = 0
			continue
	
	return Matrix

def MatrixToFile(path, n):
	Matrix = problem2(n)
	with open(path, "w") as f:
		tempStr = ""
		for i in range(len(Matrix)):
			for j in range(len(Matrix[i])):
				tempStr += str(Matrix[i][j]) + ";"
			f.write(tempStr+"\n")
			tempStr = ""


def isValid(num, lenght):
	return (num < lenght and num >= 0)

MatrixToFile("adv3out.txt", 10)