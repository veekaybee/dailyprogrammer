"""
Analyzes descriptive numbers and outputs self-descriptive numbers
in a range of values
Daily Programmer #250: Self-descriptive numbers
"""

def return_descriptive_num(n):
	"""returns descriptive numbers based on input"""
	wholenum = ''
	n = str(n)
	for value in range(0, len(n)):
		value = str(value)
		if value in n:
			j = n.count(value)
		else:
			 j = 0
		wholenum += str(j)
	return wholenum



def check_descriptive_range(n):
	"""loops through upper and lower bound based on main() input
	of how many places in the number are needed
	"""
	upper_bound = 10 ** n 
	lower_bound = upper_bound - (9 * (10 **(n-1)))
	not_found = True
	for candidate in xrange (lower_bound, upper_bound):
		if str(candidate) == return_descriptive_num(candidate):
			not_found = False
			print candidate
	if not_found:
		print 'No self-descriptive number found'


def main():
	check_descriptive_range(2)


if __name__ == '__main__':
	main()

