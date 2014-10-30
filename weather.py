def weatherMessage(temp, low, med):
	if temp < 3:
		print ("Do stuff")
	elif temp < 10:
		print ("Do things")
	else:
		print ("Wander around in a bemused fashion")

weatherMessage (15, 7, 15)

mylist = range (0,100)
for temp in mylist:
	weatherMessage(temp, 7,15)

import random

def predictTomorrowsTemp():
	return random.choice (range(-3,25))
