#!/usr/bin/env python

import os
import time

class Logger(object):
		
	def __init__(self, filename,  priority='DEBUG', datetime=True, scriptname=True):

	# set dict of priorities correlated with integer values
		priorities = {
			'DEBUG' : 1,
			'INFO' : 2,
			'WARNING' : 3,
			'ERROR' : 4,
			'CRITICAL' : 5
			}
			
	# try to open the file; raise an error if it can't be found
		try:
			fh=open(filename, 'a')
			self.fh = fh
		except IOError, e:
			raise IOError("file can't be opened: {}".format(e))
		
	# try to set the priority integer value by checking against dict; raise an error if priority name can't be found
		try:
			new_priority = int(priorities[priority])
			self.new_priority = new_priority
		except KeyError:
			raise KeyError("{} is not a valid priority. Please use one of the following levels: {}".format(priority, list(priorities.keys())))
		
	# get the datetime if needed; raise an error if flag is not a bool
		try:
			if datetime == True:
				self.new_datetime = time.ctime()
			if datetime == False:
				self.new_datetime = ''
		except:
			raise NameError("The datetime flag {} is not a boolean. Please provide a boolean flag of True or False.".format(datetime))
			
	# get the scriptname if needed; raise an error if flag is not a bool	
		try:
			if scriptname == True:
				self.new_scriptname = filename
			if scriptname == False:
				self.new_scriptname = ''
		except:
			raise NameError("The scriptname flag {} is not a boolean. Please provide a boolean flag of True or False.".format(scriptname))
		

	# create methods for all of the different log levels	
	def debug(self, msg):
		self.write_log(msg, 1)			
	
	def info(self, msg):
		self.write_log(msg, 2)			
	
	def warning(self, msg):
		self.write_log(msg, 3)			
	
	def error(self, msg):
		self.write_log(msg, 4)			
	
	def critical(self, msg):
		self.write_log(msg, 5)
	
	
	# write the log entry
	def write_log(self, msg, level):
	# format datetime and scriptname as a string
		head = ''
		if self.new_datetime:
			head = str(self.new_datetime + "      ")
		if self.new_scriptname:
			head += str(self.new_scriptname + "      ")
	
	# check to see if the level is high enough to warrent writing to log
		if self.new_priority >= level:
				self.fh.write(head + msg + "\n")
				self.fh.close
