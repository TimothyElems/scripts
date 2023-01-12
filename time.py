import sched, time
from datetime import timedelta

s = sched.scheduler(time.time, time.sleep)

def print_time(a="default"):
	print("From print_time", time.time(), a)

def print_some_times():
	print(time.time())
	s.enter(10, 1, print_time)
	s.enter(5, 2, print_time, argument=("positional", ))
	s.enter(5, 1, print_time, kwargs={"a" : "keyword"})
	s.run()
	print(time.time())

print_some_times()



'''

So...
	- I need to be able to set the start date to this Sabbath evening. 
	- The program runs on the start time.
	- 7 days get's added to the start time.
	- The program runs at the new start time. 
	- The program runs, while true.

'''