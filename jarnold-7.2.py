#!/usr/bin/env python

import sys
import os
import subprocess


	
def main():
	output = subprocess.check_output(['curl', sys.argv[1]])
	print output

if __name__ == '__main__':
	main()
