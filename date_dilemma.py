#Reddit Daily Programmer Challenge 245 : Easy Date Dilemma
# Part 1: https://www.reddit.com/r/dailyprogrammer/comments/3wshp7/20151214_challenge_245_easy_date_dilemma/

from dateutil.parser import parse
import time

x=['2/13/15','1-31-10','5 10 2015','2012 3 17','2001-01-01','2008/01/07']

for i in x:
	new_date = parse(i)
	print(new_date.strftime('%Y-%m-%d'))

