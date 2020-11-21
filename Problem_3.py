def isPrime (n):
	n = abs(int(n))
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for x in range (3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True


def findPrimeFactors (n):
	divFound = False
	divisors = []
	while divFound != True:
		for i in range (abs(int(n/2))):
			if isPrime (i):
				print ("{} is Prime, testing on number {}".format(i, n))
				if  n % i == 0:
					divisors.append(i)
					n = n/i
					divFound = True
					print ("{} is a divisor, new number is {}".format(i, n))
				else:
					pass
			else:
				pass
	if n == 1:
		print (divisors)
	else:
		divFound = False
