#!/usr/bin/python

import sys

	
def populate(set):
	start = 0
	end = 100
	while start <= end:
		set.append(start)
		start += 1
	return set
	
def guess(number, answer, set):
	if len(set) == 1:
		print ("You changed your number! No fair :( ")
		sys.exit(0)
	else:
		number = int(number) - set[0]
		if answer == "higher":
			new_set = set[number+1:]
		if answer == "lower":
			new_set = set[:number]
	return new_set
		
		
def validate(number):
	while True:
		answer = raw_input("Is your number " + str(number) + "? : ")
		if answer.strip() in ("yes", "no"):
			break
		else:
			print("Sorry, I didn't understand that. Please type 'yes', or 'no'.")
			continue
	return answer
				
				
def highorlow(number):
	while True:
		answer = raw_input("Is your number higher or lower than " + str(number) + "? : ")
		if answer.strip() in ("higher", "lower"):
			break
		else:
			print("Sorry, I didn't understand that. Please type 'higher', or 'lower'.")
			continue
	return answer
		
		
def new_guess(set):
	if len(set) % 2 == 0:
		middle = len(set)/2
		adjusted = middle
		new_guess = set[adjusted-1]
	if len(set) % 2 != 0:
		middle = (len(set)+1)/2
		adjusted = middle-1
		new_guess = set[adjusted]
	return new_guess
			
			
def number_guesser(set, number):
	answer = highorlow(number)
	set = guess(number, answer, set)
	number = new_guess(set)
	success = validate(number)
	if success == "yes":
		print ("I WINNNNNNNNNN!!!!!!")
	if success == "no":
		number_guesser(set, number)

	
def initialize():
	print("Let's play! Pick a number between 1 and 100 and I'll see if I can guess it.")
	set = []
	number = 50
	populate(set)
	number_guesser(set, number)
	
	
initialize()
