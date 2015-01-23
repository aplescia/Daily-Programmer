#1.12.2015

def isISBN(string):
	if (len(string) != 13):
		print "no"
	else:
		i = 10
		theSum = 0
		for x in string:
			if x.isdigit():
				theSum += i * int(x)
				i -= 1
		if theSum % 11 == 0:
			print "yes"
		else:
			print "no"

isISBN("0-7475-3269-9")