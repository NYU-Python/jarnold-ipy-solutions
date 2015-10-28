#!/usr/bin/python

import sys


def guess(number, answer, set):
	if max(set) - min(set) <= 1:
		print ("You changed your number! No fair :( ")
		sys.exit(0)
	else:
		number = number - set[0]
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
	print set
	if len(set) % 2 == 0:
		middle = len(set)/2
		new_guess = set[middle]
	if len(set) % 2 != 0:
		middle = (len(set)+1)/2
		new_guess = set[middle-1]
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
	set = range(100)
	number = 50
	number_guesser(set, number)
	
	
initialize()
