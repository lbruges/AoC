def problem1(path):
	jumpOffsets = list(map(int, readFile(path)))
	
	steps = 0
	i = 0 
	while i < len(jumpOffsets):
		steps += 1
		actualValue = jumpOffsets[i]
		jumpOffsets[i] += 1
		i += actualValue

	print(steps)

def problem2(path):
	jumpOffsets = list(map(int, readFile(path)))
	
	steps = 0
	i = 0 
	while i < len(jumpOffsets):
		steps += 1
		actualValue = jumpOffsets[i]
		if actualValue < 3:
			jumpOffsets[i] += 1
		else:
			jumpOffsets[i] -= 1
		
		i += actualValue

	print(steps)


def readFile(path):
	with open(path, "r") as f:
		temp = f.read().splitlines()
	return temp

problem2("inputDay5.txt")