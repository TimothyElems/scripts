import time
import math

def calcProd():
	# Calculate the product of the first 100,000 numbers
	product = 1
	n = 100000
	for i in range(1, n):
		product = product * i
	return product
	# return sum(range(1, 100000))



startTime = time.time()
prod = calcProd()
endTime = time.time()
print("The result is %s digits long" % (len(str(prod))))
print("Took %s seconds to calculate" % (endTime - startTime))