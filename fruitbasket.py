#Reddit Daily Programmer Challenge 242
# https://www.reddit.com/r/dailyprogrammer/comments/3v4zsf/20151202_challenge_243_intermediate_jennys_fruit/

import itertools

#Solve for optimal basket combinations based on limit of $5.00 - 500 pennies
#0-1 variation of original challenge knapsack problem 
basket = {"apple": 59,
"banana": 32,
"coconut": 155,
"grapefruit": 128,
"jackfruit": 1100,
"kiwi": 41,
"lemon": 70,
"mango": 97,
"orange": 73,
"papaya": 254,
"pear": 37,
"pineapple": 399,
"watermelon": 500}


def value_loop(fruitdict):
	'''
	Loops through dictionary values and returns combination sets
	that add up to 500 cents
	'''
	for R in range(1, len(basket.values())+1):
		for i in itertools.combinations(basket.iteritems(),R):
			if sum(x[1] for x in i) == 500:
				print list((x[0] for x in i))


if __name__ == '__main__':
	value_loop(basket)


