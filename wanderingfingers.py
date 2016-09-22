'''
Reddit Daily Programming Challenge 284
Wandering Fingers
http://bit.ly/2dcaVXH
'''


def match_inputs(input_string, filename):
	'''
	Function takes filename (dictionary of words) 
	as input to compare to typed input (input_string)
	'''
	first_letter = input_string[0]
	last_letter = input_string[-1]

	with open(filename,"r") as ngrams:
		for line in ngrams:
			word = line.rstrip()
			# Strip first and last letters once they match
			if len(word) >= 5 and word[0] == first_letter and word[-1] == last_letter:
				i = 1 #counter to count matched characters
				for c in input_string[1:-1]:
					if c == word[i]:
						i += 1
						if i == len(word) - 2:
							print word
					
match_inputs('qwertyuytresdftyuioknn',"ngrams.txt")
match_inputs('gijakjthoijerjidsdfnokg',"ngrams.txt")


