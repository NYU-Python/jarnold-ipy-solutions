#!/usr/bin/python

import csv
import sys


tickers = ['AAPL', 'FB', 'GOOG', 'LNKD', 'MSFT']
summaries = ['centered', 'average', 'max', 'min', 'median']
set = []
	
def populate(set):
	start = 0
	end = 251
	while start <= end:
		set.append(str(start))
		start += 1
	return set

def stock_price_summary(myinput):
	type = myinput[0]
	days = int(myinput[1])
	ticker = myinput[2]
	if type == "centered":
		print get_centered(get_data(ticker, days))
	if type == "max":
		print max_price(get_data(ticker, days))
	if type == "min":
		print min_price(get_data(ticker, days))
	if type == "average":
		print simple(get_data(ticker, days))
	if type == "median":
		print get_median(get_data(ticker, days))

def get_data(ticker, days):
	prices = []
	selected_days = []
	flat_selected_days = []
	flat_prices = []
	tkr = ticker.lower()
	filename = str(tkr) + '.csv'
	for line in open(filename):
		text = line.strip().split(',')
		prices.append(text[1:5])
	top_limit = int(days) + 1
	selected_days.append(prices[1:top_limit])
	flat_selected_days = [val for sublist in selected_days for val in sublist]
	flat_prices = [val for sublist in flat_selected_days for val in sublist]
	for item in flat_prices:
		item = float(item)
	prices = flat_prices
	return prices

def max_price(prices):
	prices.sort()
	max = prices.pop()
	return max
	
def min_price(prices):
	prices.sort(reverse=True)
	min = prices.pop()
	return min
	
def average(first, second):
	num = float(first) + float(second)
	return num/2

def simple(prices):
	total = sum(float(item) for item in prices)
	length = len(prices)
	return total/length

def get_median(prices):
	prices.sort()
	length = len(prices)
	if length % 2 == 0:
		middle = length/2
		m = prices[middle:middle+1]
		return average(prices[0], prices[1])
	elif length % 2 != 0:
		 m = length+1
		 m = m/2 - 1
		 return prices[m]

def get_centered(prices):
	s = set(prices)
	prices = list(prices)
	return get_median(prices)	
	
def valid():
	while True:
		myinput = raw_input("Please type in a summary type, a number of days, and a ticker name: ")
		myinput = myinput.split()
		print myinput
		if len(myinput) == 3:
			type = myinput[0]
			days = myinput[1]
			ticker = myinput[2]
			if (str(type) in summaries and 
				str(days) in set and 
				str(ticker) in tickers):
				break
			if str(type) not in summaries:
				print ("I don't understand that summary type. Please type 'centered', 'average', 'max', 'min', or 'median'.")
				continue
			if str(days) not in set:
				print ("Sorry! Your number of days must be an integer equal to or less than 251.")
				continue
			if str(ticker) not in tickers:
				print ("I don't understand that ticker name. Please type 'AAPL', 'FB', 'GOOG', 'LNKD', or 'MSFT'.")
				continue
			else:
				break
		else:
			continue
	return myinput	

def initialize():
	populate(set)
	myinput = valid()
	stock_price_summary(myinput)
	
	
initialize()
