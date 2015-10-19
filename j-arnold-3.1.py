#usr/bin/python2.7

import os
import sys
import argparse


# Using argparse to validate arguments
def getArgs():
	parser = argparse.ArgumentParser(description="Reads a directory and then presents the files sorted by one of three criteria: filename, file size or last modification time.")
	parser.add_argument('directory', action='store', help='give location of desired directory')
	parser.add_argument('direction', action='store', help='give sort criteria for directory', choices=['ascending', 'descending'])
	parser.add_argument('criteria', action='store', help='give sort direction of directory', choices=['size', 'mtime', 'name'])
	return parser.parse_args()


# Building the dictionary of dictionaries	
def build_dict(mydir):
	try:
		outerdict = {}
		for file in os.listdir(mydir):
			fullpath = os.path.join(mydir, file)
			innerdict = {}
			innerdict['size'] = os.path.getsize(fullpath)
			innerdict['mtime'] = os.path.getmtime(fullpath)
			innerdict['name'] = str(file).lower()
			outerdict[file] = innerdict
		return outerdict
	except OSError:
		print "Sorry, that directory doesn't exist. Please enter a valid directory."
		sys.exit()


# Getting results based on criteria and direction	
def getresults(mydict, crit, direction):
	if direction == "ascending":
		print sorted(mydict, key=lambda x:mydict[x][crit])
	if direction == "descending":
		print sorted(mydict, key=lambda x:mydict[x][crit], reverse=True)


def main():
	argvals = getArgs()
	mydir = argvals.directory
	direction = argvals.direction
	crit = argvals.criteria
	mydict = build_dict(mydir)
	getresults(mydict, crit, direction)
		

main()
