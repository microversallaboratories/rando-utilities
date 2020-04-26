#rand_n

#IMPORT

# seed the pseudorandom number generator
from random import seed
from random import random
from random import randint
# seed random number generator
seed(1)

#MAIN
upper = int(0)
again = bool(1)

# generate some random numbers
while(again):
	upper = input("What upper range would you like?: ")
	value = randint(0,upper)
	print(value)
	again = input("Another number? 1-yes, 0-no: ")
