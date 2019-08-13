"""
Purpose: Learning test cases in python
"""
import unittest

class SimpleTest(unittest.TestCase): 

	# Returns True or False. 
	def test(self):		 
		self.assertTrue(False) 

if __name__ == '__main__': 
	unittest.main() 
