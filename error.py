'''
def sum(x, y):
	total = 0
	total = total + x + y
	return total

print(sum(2, 4))
'''


'''

I need to dip my feet or fully submerge myself in Errors and Exceptions. I have an initial feeling of shying-away, so I guess this is the right path. I had the same feels with Regular Expressions and they proved to not be too difficult.


'''

# With the try statement, first the `try` clause is executed
# If there're no exceptions, the except clause is skipped
# If an exception occurs during the try, the rest of the clause is skipped and the except is executed. If the exception matches the exception clause, then the attached message prints
# If the exception occurs and their is no match, the exception is passed to `outer try statements`. 

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Ain't no love in the heart of a city. Try again.")

# This one is ran with multiple except clauses
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except (RuntimeError, TypeError, EOFError, Exception, IOError,ValueError, IndexError, KeyError, KeyboardInterrupt, NameError, StopIteration, TypeError, ValueError, ZeroDivisionError):
        print("Ain't no love in the heart of a city. Try again.")
