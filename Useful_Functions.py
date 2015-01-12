"""
	Useful Python Functions for 
	Reddit.com/r/dailyprogrammer 
	by Anthony Plescia

"""
#returns a list containing the digits of a number
def getDigits(x):
	digits = []
	strVersion = str(x)
	for digit in strVersion:
		int(digit)
		digits.append(digit)
	return digits

#returns a list containing values found in a string	
def getValues(x):
	vals = []
	newString = x.split()
	print newString
	for item in newString:
		try:
			value = int(item)
			vals.append(item)
		except ValueError:
			pass
	return vals

#removes all occurences of a substring within a string
def removeSub(x, *args):
	argument = x
	for i in args:
		argument = argument.replace(i, '')
	return argument

#returns a list containing all given factors of a number
def factors(x):
	factorlist = []
	xcpy = x
	#add number itself to list
	factorlist.append(xcpy)
	print xcpy
	#list for factors
	
	#iterates through integer factors, adding them to list
	while xcpy > 1:
		xcpy-=1
		if x % xcpy == 0:
			factorlist.append(xcpy)
	
	#adds 1 to list (base case)
	factorlist.append(1)
	return factorlist