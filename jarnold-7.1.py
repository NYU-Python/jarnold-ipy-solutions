#!/usr/bin/env python

import sys
import os
import timeit


fh = sys.argv[1]

def listcomp(f_name):
	text = open(os.path.abspath(fh)).readlines()
	for item in text:
		item.rstrip('".,;:?!\n\'').lower()
	return text

def forloop(f_name):
	text = open(os.path.abspath(fh)).readlines()
	processed_list = []
	for item in text:
		processed_list.append((item.rstrip('".,;:?!\n\'')).lower())
	return processed_list


def gencomp(f_name):
	text = open(os.path.abspath(fh)).readlines()
	my_gen = ((item.rstrip('".,;:?!\n\'')).lower() for item in text)
	processed_list = list(my_gen)
	return processed_list


def mapfunc(f_name):
	text = open(os.path.abspath(fh)).readlines()
	processed_list = map(lambda x: x.rstrip('".,;:?!\n\'').lower(), text)
	return processed_list


	
def main():
	print timeit.timeit('listcomp(fh)', setup='from __main__ import listcomp, fh', number=10)
	print timeit.timeit('forloop(fh)', setup='from __main__ import forloop, fh', number=10)
	print timeit.timeit('gencomp(fh)', setup='from __main__ import gencomp, fh', number=10)
	print timeit.timeit('mapfunc(fh)', setup='from __main__ import mapfunc, fh', number=10)

if __name__ == '__main__':
	main()
