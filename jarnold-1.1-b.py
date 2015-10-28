#!/usr/bin/python

import csv
import sys


tickers = ['AAPL', 'FB', 'GOOG', 'LNKD', 'MSFT']
summaries = ['centered', 'average', 'max', 'min', 'median']
set = []
	

def stock_price_summary(myinput):
	type, days, ticker = myinput
	prices = get_data(ticker, days)
	if type == "centered":
		print get_centered(prices)
	if type == "max":
		print max_price(prices)
	if type == "min":
		print min_price(prices)
	if type == "average":
		print simple(prices)
	if type == "median":
		print get_median(prices)

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
	max = prices.max()
	return max
	
def min_price(prices):
	min = prices.max()
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
	
def valid(myset):
	while True:
		myinput = raw_input("Please type in a summary type, a number of days, and a ticker name: ")
		myinput = myinput.split()
		print myinput
		if len(myinput) == 3:
			type, days, ticker = myinput
			if (type in summaries and 
				days in myset and 
				ticker in tickers):
				break
			if type not in summaries:
				print ("I don't understand that summary type. Please type 'centered', 'average', 'max', 'min', or 'median'.")
				continue
			if days not in myset:
				print ("Sorry! Your number of days must be an integer equal to or less than 251.")
				continue
			if ticker not in tickers:
				print ("I don't understand that ticker name. Please type 'AAPL', 'FB', 'GOOG', 'LNKD', or 'MSFT'.")
				continue
			else:
				break
		else:
			continue
	return myinput	

def main():
	myset = [ str(x) for x in range(252) ]
	myinput = valid(myset)
	stock_price_summary(myinput)
	
	
main()
