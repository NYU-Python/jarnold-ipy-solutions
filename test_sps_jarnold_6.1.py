#!/usr/bin/env python

"""
NAME
    test_sps.py

DESCRIPTION
    Tests for stock_price_summary.py homework solution

AUTHOR
    Jessica Arnold
"""

import os
import stock_price_summary as sps
import pytest



# GOOD DATA

VALID_FILENAME = 'appl.csv'
VALID_TICKER = 'aapl'
NUMERIC_LIST = [1, 2, 3]
EVEN_NUMERIC_LIST = [1, 2, 3, 4]
LIST_DUPLICATES = [1, 2, 3, 3, 4]
LIST_DUPLICATES_TWO = [1, 2, 1, 4, 3, 4]
GOOD_ARGS = ('summary', 5, 'ticker')

# BAD DATA

BAD_ARGS = ('summary', 5)
INVALID_FILENAME = 'some_bad_filename'
CAPPED_FILENAME = 'AAPL'
LOWER_FILENAME = 'aapl'
NON_NUMERIC_LIST = [1, 2, 3, 'a']
NON_STRING = 5
NON_ITERABLE = 5
NON_NUMBER = '5'
NON_VALID_NUM = 'blah'
INVALID_TICKER = 'an_invalid_ticker'




# Test Functions

def test_acquire_data():

    # Testing on an invalid filename
    with pytest.raises(IOError):
        sps.acquire_data(INVALID_FILENAME, 0) 

    # Number of days not a valid data type
    with pytest.raises(TypeError):
    	filename = sps.get_filename_from_ticker(VALID_TICKER)
        sps.acquire_data(filename, NON_NUMERIC_LIST) 
	
    # Number is greater than number of entries in file
    with pytest.raises(ValueError):
    	filename = sps.get_filename_from_ticker(VALID_TICKER)
        sps.acquire_data(filename, 300) 
	
    # Number is greater than number of entries in file
    with pytest.raises(ValueError):
    	filename = sps.get_filename_from_ticker(VALID_TICKER)
        sps.acquire_data(filename, 300) 
	
    # Assert that data is as expected
    filename = sps.get_filename_from_ticker(VALID_TICKER)
    assert sps.acquire_data(filename, 5) == [114.71, 115.0, 114.32, 113.4, 115.21]
	
	
	
def test_is_all_numbers():

    # Not a valid list of values
    with pytest.raises(TypeError):
        sps.is_all_numbers(NON_ITERABLE) 

    # Assert that when all vals are number, returns True
    assert sps.is_all_numbers(NUMERIC_LIST) == True
    
    # Assert that when all vals are number, returns False
    assert sps.is_all_numbers(NON_NUMERIC_LIST) == False



def test_get_median():

    # Not a valid list of values
    with pytest.raises(TypeError):
        sps.get_median(NON_ITERABLE) 

    # Vals contain non-numbers
    with pytest.raises(TypeError):
        sps.get_median(NON_NUMERIC_LIST) 
    
    # Assert that even number returns correct val
    assert sps.get_median(EVEN_NUMERIC_LIST) == 2.5
    
    # Assert that odd number returns correct val
    assert sps.get_median(NUMERIC_LIST) == 2


def test_get_centered():

    # Not a valid list of values
    with pytest.raises(TypeError):
        sps.get_centered(NON_ITERABLE) 

    # Vals contain non-numbers
    with pytest.raises(TypeError):
        sps.get_centered(NON_NUMERIC_LIST) 
    
    # Returns correct value in case of duplicates
    assert sps.get_centered(LIST_DUPLICATES) == 2.5
    
    # Returns correct value in case of duplicates
    # in top and bottom vals
    assert sps.get_centered(LIST_DUPLICATES_TWO) == 2.5
    
    # Returns correct value from standard list
    assert sps.get_centered(NUMERIC_LIST) == 2
    


def test_get_average():

    # Not a valid list of values
    with pytest.raises(TypeError):
        sps.get_average(NON_ITERABLE) 

    # Vals contain non-numbers
    with pytest.raises(TypeError):
        sps.get_average(NON_NUMERIC_LIST) 
    
    # Assert that good list returns correct val
    assert sps.get_average(NUMERIC_LIST) == 2
    


def test_get_filename_from_ticker():

    # Not a valid argument string
    with pytest.raises(AttributeError):
        sps.get_filename_from_ticker(NON_STRING) 
        
    # Uppercase ticker returns correct val
    assert sps.get_filename_from_ticker(CAPPED_FILENAME) == '/Users/jarnoldmbp/Desktop/stock_prices/aapl.csv'
   
   # Lowercase ticker returns correct val
    assert sps.get_filename_from_ticker(LOWER_FILENAME) == '/Users/jarnoldmbp/Desktop/stock_prices/aapl.csv'

	
	

def test_validate_args():

    # Testing on an bad summary type
    with pytest.raises(ValueError):
        sps.validate_args(NON_ITERABLE, 5, VALID_TICKER)

    # Testing on an invalid ticker name
    with pytest.raises(IOError):
        sps.validate_args('average', 5, INVALID_TICKER)

    # Number of days not a valid data type
    with pytest.raises(ValueError):
        sps.validate_args('average', NON_VALID_NUM, VALID_TICKER)
        
    # Assert correct value provided
    assert sps.validate_args('centered', 5, VALID_TICKER) == 114.71
	


def test_parse_args():

    # Bad number of args fails
    with pytest.raises(TypeError):
        sps.validate_args(BAD_ARGS)

    # Good number of args passes
    assert sps.parse_args(GOOD_ARGS) == ('summary', 5, 'ticker')
