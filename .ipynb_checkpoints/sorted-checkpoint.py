'''

i am trying to make a script that takes all the files in my Downloads dir and moves them into separate dirs, that way their is further organization

steps
	+ access all donwloads
	+ create new folders
	+ move a file into desired location
	+ move all certain filetypes into a certain subdir
		- i do not know how to move all files with a certain ending... regex
	- next up, make the process automatic
		- sync it up to a timeline... every saturday night by 20:00
		- there is a module called `sched`! i'm giving it a go


libraries
	- os. This library is for getting access to the things that are on the system. The Doc says it is for 'miscellaneous operating system interfaces,' I use it to get access to directories and their contents.

	- shutil. This is for file manipulation. The Doc says it "offers a number of high-level operations on files and collections of files". I use it for move the files to new directories.

'''

import os
import shutil
import sched
import datetime as dt
import time
import calendar

source_dir = "/Users/elems/Downloads"
new_movie_dir = "/Users/elems/Downloads/Movies"
zip_dir = "/Users/elems/Downloads/Zipped"
soft_dir = "/Users/elems/Downloads/Software"
anki_dir = "/Users/elems/Downloads/Anki"


# The following code works!
def sort_movies():
	with os.scandir(source_dir) as entries:
		for entry in entries:
			if entry.name.endswith('.mp4'):
				shutil.move(entry, "/Users/elems/Downloads/Movies")
			print(entry.name)

def sort_ebooks():
	with os.scandir(source_dir) as entries:
		for entry in entries:
			if entry.name.endswith('.pdf'):
				shutil.move(entry, "/Users/elems/Downloads/eBooks/PDFs")
			elif entry.name.endswith('.epub'):
				shutil.move(entry, "/Users/elems/Downloads/eBooks/ePubs")
			elif entry.name.endswith('.mobi'):
				shutil.move(entry, "/Users/elems/Downloads/eBooks/Mobi")
			print(entry.name)

def sort_zips():
	with os.scandir(source_dir) as entries:
		for entry in entries:
			if entry.name.endswith('.zip'):
				shutil.move(entry, zip_dir)
			elif entry.name.endswith('.rar'):
				shutil.move(entry, zip_dir)
			print(entry.name)

def sort_softwares():
	with os.scandir(source_dir) as entries:
		for entry in entries:
			if entry.name.endswith('.dmg'):
				shutil.move(entry, soft_dir)
			elif entry.name.endswith('.pkg'):
				shutil.move(entry, soft_dir)
			print(entry.name)

def sort_ankis():
	with os.scandir(source_dir) as entries:
		for entry in entries:
			if entry.name.endswith('.apkg'):
				shutil.move(entry, anki_dir)
			print(entry.name)


def run_time():
	calendar.setfirstweekday(calendar.SUNDAY)
	rt = dt.timedelta(7)
	og_date = dt.datetime(2022, 11, 5, 20, 0, 0)
	og_date = calendar.SATURDAY
	og_time = og_date.
	current_date = datetime.datetime.now()
	


# for my final trick, i will turn these processes into functions and call the functions
def main():

	sort_movies()
	sort_ebooks()
	sort_zips()
	sort_softwares()
	sort_ankis()	

if __name__ == "__main__":
	main()