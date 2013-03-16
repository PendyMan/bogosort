#!/usr/bin/env python
# encoding: utf-8
"""
test.py

Created by Kyle Nickel on 2013-03-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from bogo import Bogo

def main():
	data = [1, 3, 2]
	bogo = Bogo(data, True)
	bogo.sort()


if __name__ == '__main__':
	main()

