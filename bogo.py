#!/usr/bin/env python
# encoding: utf-8
"""
bogo.py

Created by Kyle Nickel on 2013-03-16.

TODO: Need to make this a module instead of a class
"""
import random 

class Bogo(object):
	"""Our very basic object that will be doing the sorting"""
	
	debug = False
	def __init__(self, data, debug=False):
		self.data = data
		self.debug = debug 
		
	def sort(self):
		"""Our sorting loop, continue to randomize until it is sorted"""
		while not self.check_if_sorted():
			self.randomize()
		print "Sorted..."
		
		
	def check_if_sorted(self):
		"""Run through the list to see if it is sorted and return our findings"""
		for number in range(len(self.data)):
			if number + 1 < len(self.data):
				if self.data[number] > self.data[number + 1]:
					return False

		return True
					
	def randomize(self):
		"""Randomize the order of our data"""
		if self.debug:
			print "Randomizing"
		for number in range(len(self.data)):
			temp_stored_number = self.data[number]
			swap_index = random.randrange(len(self.data))
			
			self.data[number] = self.data[swap_index]
			self.data[swap_index] = temp_stored_number
