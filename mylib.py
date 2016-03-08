#!/usr/bin/env python

import os

"""

Class PersistDict inherits from dict and provides a "persistent
dictionary". When the dictionary is instantiated, a filename is passed to the
constructor. Every write to the dictionary writes the dictionary to the file. 

"""


class PersistDict(dict):
	
	def __init__(self, filename):
	
	# Initialize PersistDict as a class inheriting from dict
		dict.__init__(self)
		
	# Sets up a filename in case one is not provided
		if not filename:
			self.my_name = "PersistDict.txt"
		elif filename:
			self.my_name = filename
			
	def __setitem__(self, key, value):
		dict.__setitem__(self, key, value)
		self.write_file()	
				
	def __getitem__(self, key):
		my_name = self.my_name
		my_persis_dict = {}
		
	# Get the perviously constructed file
		for line in open(my_name, 'r'):
		
	# Read the info from the file into a new dictionary
			my_info = line.strip().split('=', 1)
			my_key = str(my_info[0])
			my_val = str(my_info[1])
			dict.__setitem__(self, my_key, my_val)
		print dict.__getitem__(self, key)
	
	def __delitem__(self, key):
		dict.__delitem__(self, key)
		self.write_file()	
	
	def __setdefault__(self, key, value):
		if not value:
			value = 0
			dict.__setdefault__(self, key, value)
			self.write_file()
		elif value:
			dict.__setdefault__(self, key, value)
			self.write_file()

	def update(self, newdict): 
		dict.update(self, newdict)
		self.write_file()	
	
	def clear():
		dict.clear(self)
		self.write_file()	

	# Write_file class is called internally every time we need to
	# write to the persistent dictionary file
	def write_file(self):
		my_name = self.my_name
		with open(my_name, 'w') as file:
			for item in self:
				my_value = dict.__getitem__(self, item)
				file.write(str(item) + "=" + str(my_value) + "\n")
				
	
	
