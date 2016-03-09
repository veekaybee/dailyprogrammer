""" 
Reddit Daily Programmer #257
Dead Presidents
http://bit.ly/1Xd2qqP
"""


# read CSV, parse birth and death year, append values to list

with open('presidents.csv','r') as f:
	next(f) #skip header row
	all_years = []	
	for line in f:
		line = line.split(',')
		b = int(line[1][-4:])
		try:
			d = int(line[3][-4:])
		except ValueError: # skip blank years
			d = 0
		for x in range(b,d+1):
 			all_years.append(x)
	

# convert list to dictionary, pick max years from dictionary
y = {}

for year in all_years:
	if year not in y:
		y[year] = 1
	else: 
		y[year] += 1

highest = max(y.values()) #picks multiple max values

print ([k for k,v in y.items() if v == highest])
