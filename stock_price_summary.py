#!/usr/bin/env python

"""
NAME
    stock_price_summary.py

DESCRIPTION
    loop through a file of stock prices and derive average, median, etc.

AUTHOR
    David Blaikie (dbb212@nyu.edu)
"""


import os
import sys
import pdb

# CHANGE THIS VALUE TO YOUR RELATIVE PATH LOCATION
data_dir = '/Users/jarnoldmbp/Desktop/stock_prices'

output_precision = 2
summary_types = ['max', 'min', 'average', 'centered', 'median']
file_extension = '.csv'


def acquire_data(filename, days):
    """ retrieve list of closing prices from this ticker's history file """

    fh = open(filename)

    ticks = []
    for line in fh.readlines()[1:]:
        els = line.split(',')
        ticks.append(float(els[-2]))

    fh.close()

    days = int(days)
    if len(ticks) < days-1:
        raise ValueError, '{} days is more than available in data source'.format(days)

    prices = ticks[0:days]
    return prices


def is_all_numbers(vals):
    for val in vals:
        if not isinstance(val, (int, float, long)):
            return False
    return True


def get_median(prices):
    """ given a list of prices, calculate the median """
    
    if not is_all_numbers(prices):
        raise TypeError('get_median():  input not all numbers')
    prices = sorted(prices)
    middleish = len(prices) / 2
    if len(prices) % 2:
        return prices[middleish]
    return (prices[middleish-1] + prices[middleish]) / float(2)


def get_centered(prices):
    """ given a list of prices, calculate the centered average """

    if not is_all_numbers(prices):
        raise TypeError('get_centered():  input not all numbers')
    prices = set(prices)
    prices = sorted(prices)[1:-1]
    return get_median(prices)


def get_average(prices):
    return sum(prices) / len(prices)


def get_filename_from_ticker(ticker):
    """ given a file ticker, combine with data dir and file extension """

    filename = os.path.join(data_dir, ticker.lower() + file_extension)
    return filename


def validate_args(type, days, ticker):
    """ normalize and validate user arguments """

    if type not in summary_types:
        raise ValueError, 'validate_args():  type "{}" not found'.format(type)

    filename = get_filename_from_ticker(ticker)

    if not os.path.isfile(filename):
        raise IOError, 'validate_args():  stock ticker "{}" could not be found'.format(ticker)

    # select just n number of prices from list
    if not days.isdigit():
        raise ValueError, 'validate_args():  days arg must be an integer'

    return filename


def parse_args(args):

    if len(args) != 3:
        raise IndexError, 'parse_args():  arguments missing'
    type, days, ticker = args
    return type, days, ticker


def main(args):
    """ perform summary calculation """

    type, days, ticker = parse_args(args)

    filename = validate_args(type, days, ticker)

    prices = acquire_data(filename, days)

    if type == 'max':
        return_val = max(prices)
    if type == 'min':
        return_val = min(prices)
    if type == 'average':
        return_val = get_average(prices)
    if type == 'centered':
        return_val = get_centered(prices)
    if type == 'median':
        return_val = get_median(prices)

    print round(return_val, output_precision)


if __name__ == '__main__':

    main(sys.argv[1:])

