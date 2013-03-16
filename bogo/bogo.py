#!/usr/bin/env python
# encoding: utf-8
"""
bogo.py

Created by Kyle Nickel on 2013-03-16.
Copyright (c) 2013 Kyle Nickel. All rights reserved.
"""
import random 
		
def sort(data):
	"""Our sorting loop, continue to randomize until it is sorted"""
	while not check_if_sorted(data):
		data = randomize(data)
	print "Sorted..."
		
		
def check_if_sorted(data):
	"""Run through the list to see if it is sorted and return our findings"""
	for number in range(len(data)):
		if number + 1 < len(data):
			if data[number] > data[number + 1]:
				return False

	return True
					
def randomize(data):
	"""Randomize the order of our data"""
	print "Randomizing"
	for number in range(len(data)):
		temp_stored_number = data[number]
		swap_index = random.randrange(len(data))
			
		data[number] = data[swap_index]
		data[swap_index] = temp_stored_number
		return data