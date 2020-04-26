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
num = int(0)
numlist = []

upper = input("What upper range would you like?: ")
num = input("How many numbers would you like?: ")

# generate some random numbers
for _ in range(num):
	value = randint(0,upper)
	numlist.append(value)

print(numlist)
