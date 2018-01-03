def firstProblem(text):
	total = 0
	
	for i in range(len(text)-1):
		if text[i] == text[i+1]:
			total += int(text[i])

	if text[0] == text[len(text)-1]:
		total = total + int(text[0])
	
	print(total)

	'''
	for i in range(len(text)-1):
		if text[i] == text[i+1]:
			subtotal += int(text[i])
		else:
			total += subtotal
			subtotal = 0

	total += subtotal

	if text[0] == text[len(text)-1]:
		total = total + int(text[0])
	
	print(total)
	'''

def secondProblem(text):
	total = 0 

	windowSize = int(len(text)/2)
	
	for i in range(len(text)-windowSize):
		if(text[i] == text[i+windowSize]):
			total += int(text[i])*2

	print(total)
	
def swap(num1, num2):
	num1 = num1 + num2
	num2 = num1 - num2
	num1 = num1 - num2
	print(num1)
	print(num2)

#text = input()
#firstProblem(text)
swap(2, 3)