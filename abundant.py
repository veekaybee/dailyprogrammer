#Reddit Daily Programmer Challenge 243 : Abundant and Deficient Numbers
#https://www.reddit.com/r/dailyprogrammer/comments/3uuhdk/20151130_challenge_243_easy_abundant_and/

#Python 2.7 locally
from __future__ import division

def factors(n):    
	divisors = []
	for i in xrange(1, n+1):
		if n % i == 0:
			divisors.append(i)
	return divisors

def deficient(n):
	 if sum (factors(n)) < 2*n:
	 	print '%s, deficient' % n 
	 elif sum (factors(n)) > 2*n:
	 	abundant_by = sum(factors(n)) - 2*n
	 	print '%s abundant by  %s ' % (n, abundant_by)
	 else:
	 	print '%s' % n


     
if __name__ == '__main__':
	numbers = [111,112,220,69,134,85]
	for i in numbers:
		deficient(i)

