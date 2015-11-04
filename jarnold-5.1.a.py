#!/usr/bin/env python

import os
from mylib import PersistDict


dd = PersistDict('myfile.txt') # if new file, create
dd['a'] = 6
dd['b'] = 11
