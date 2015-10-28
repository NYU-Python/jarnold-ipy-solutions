#usr/bin/python2.7

import os
import sys



def unique_cities(cities):
	# get rid of empty items
	if cities.has_key(''):
		del cities['']
		
	unique_cities = sorted(set(cities.keys()))
	return unique_cities
	

def top_ten_countries(countries):
	# get rid of empty items
	if countries.has_key(''):
		del countries['']
		
	# sort by integer of value
	top_ten_countries = sorted(countries, key=lambda i: int(countries[i]), reverse=True)
	return top_ten_countries[0:9]
	
	

def top_ten_machine_names(machine_names):
	# get rid of empty items
	if machine_names.has_key(''):
		del machine_names['']
		
	# sort by integer of value
	top_ten_machine_names = sorted(machine_names, key=lambda i: int(machine_names[i]), reverse=True)
	return top_ten_machine_names[0:9]


# find out what info the user wants

def what_would_you_like(cities, countries, machine_names):
	print """What information would you like from the bit.ly data?
a) A set of unique cities
b) The top ten most popular country codes
c) The top ten most popular machine names
"""
	answer = raw_input("Please type the letter name of your selection: ")
	
	if answer == "a":
		print unique_cities(cities)
		
	elif answer == "b":
		print top_ten_countries(countries)
		
	elif answer == "c":
		print top_ten_machine_names(machine_names)
		
	else:
		print "Sorry, I didn't get that answer"
		
	# recursively calls itself to run the prompt again
		what_would_you_like(cities, countries, machine_names)
		

def main():	
	
	# set up empty dicts 
	cities = {}
	countries = {}
	machine_names = {}
	
	# get the data from the tsv
	for line in open('bitly.tsv').readlines()[1:]:
		elements = line.strip('\n\s').split('\t')
		
	
	# read the data into the dictionaries
	
		try:
			city = elements[3]
			country = elements[4]
			machine_name = elements[2].split('/')[2]
		
			if city in cities:
				cities[city] += 1
			else:
				cities[city] = 1
				
			if country in countries:
				countries[country] += 1
			else:
				countries[country] = 1
				
			if machine_name in machine_names:
				machine_names[machine_name] += 1
			else:
				machine_names[machine_name] = 1
	
	# keep going if the information isn't found
		except:
			continue
			
	
	# provide data to user
	what_would_you_like(cities, countries, machine_names)
		


main()
