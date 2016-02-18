
'''
Reddit Daily Programming Challenge 254
Atbash Cypher
http://bit.ly/1PIHXb0
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
atbash = alphabet[::-1]

mydict = dict(zip(alphabet, atbash))

def atbash_gen(mydict, word):
	reverse = []
 	for i in word:
 		if i not in alphabet:
 			reverse.append(i)
 		else:
	 		for key, value in mydict.items():
	 			if i in key:
	 				reverse.append(value)
 	full_word = ''.join(reverse)
 	return word, full_word
		
phrase = raw_input('Enter a word to atbash: ')

print atbash_gen(mydict, phrase)
	
