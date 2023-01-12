import os

source_dir = '/Users/elems/Downloads'

with os.scandir(source_dir) as entries:
	for entry in entries:
		print(entry.name)