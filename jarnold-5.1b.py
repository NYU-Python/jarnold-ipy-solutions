#!/usr/bin/env python

import os
from mylib import PersistDict


dd = PersistDict('myfile.txt')


print dd['a'] # 5
print dd['b'] # 10
