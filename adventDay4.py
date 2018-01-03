def problem1(path):
	lines = readFile(path)
	valid = 0
	for line in lines:
		words = line.split(" ")
		wordSet = set(words)
		if len(words) == len(wordSet):
			valid += 1

	print(valid)

def problem2(path):
	valid = 0
	lines = readFile(path)
	for line in lines:
		words = line.split(" ")
		wordSet = set(map(sortAnagram, line.split(" ")))

		if len(words) == len(wordSet):
			valid += 1

	print(valid)

def readFile(path):
	with open(path, "r") as f:
		temp = f.read().splitlines()
	return temp

def sortAnagram(word):
	return "".join(sorted(word))

problem2("inputDay42.txt")