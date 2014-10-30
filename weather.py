def weatherMessage(temp, low, med):
	if temp < 3:
		print ("wear wool trousers")
	elif temp < 10:
		print ("wear trousers")
	else:
		print ("wear shorts")

weatherMessage (15, 7, 15)

mylist = range (0,100)
for temp in mylist:
	weatherMessage(temp, 7,15)

import random

def predictTomorrowsTemp():
	return random.choice (range(-3,25))
