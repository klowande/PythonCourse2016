def factorial(n):
	if n==1: return 1
	return n*factorial(n-1)
	
#Exercise 1
def GCD(a,b):	
	if b > a:
		if b % a == 0:
			return 'The GCD is %s.' % a
		else:
			return GCD(b % a, b)
	else:
		if a % b == 0:
			return 'The GCD is %s.' % b
		else:
			return GCD(a, a % b)

#Exercise 2
def Prime(n):
	primes = []
	less = range(n)
	if
		primes.append(n)
	else:
		return primes


#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html