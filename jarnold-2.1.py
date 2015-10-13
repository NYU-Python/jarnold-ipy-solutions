#usr/bin/python2.7

import os
import sys


sendmail_prog = '/usr/sbin/sendmail' 	

def main():	

	required_args = set(['to', 'from'])
	valid_args = set(['to', 'from', 'subject', 'body'])
	args = sys.argv[1:]
	
	
	# setting up the dict
	argdict = {}
	for arg in args:
		key, val = arg.split('=')
		argdict[key] = val
	
	fields = set(argdict.keys())
	
	# validating dict fields
	invalid_args = list(fields.difference(valid_args))
	required_not_present = list(required_args.difference(fields))

	# let user know if there are invalid arguments	
	if len(invalid_args) > 0:
		invalid = "{0} is not a valid argument. Valid arguments are {1}"
		print invalid.format(invalid_args, list(valid_args))

	# get the subject and body fields if none are provided
	if 'subject' not in argdict:
		argdict['subject'] = raw_input("Please type in the email subject: ")
	if 'body' not in argdict:
		argdict['body'] = raw_input("Please type in the email body: ")

	try:		
		# print out email header string, if possible
		myheader = """From: {0}
To: {1}
Subject: {2}
			"""
		
		mystr = myheader.format(argdict['from'], argdict['to'], argdict['subject'])
		print mystr
	
	except:
		# If not possible to print email header string, there must be
		# missing required arguments. Tell user what they are.
		
		if len(required_not_present) > 0:
			missing = "Missing required argument(s) {0}"
			print missing.format(required_not_present)
	

main()
