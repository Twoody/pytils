#!/usr/bin/env python3
from pytils.config import *
from pytils.tests.Tests import Tests
'''
	THIS IS A GOOD PLACE FOR DOCUMENTATION
'''

def test_XXX():
	f = '~'
	try:
		foo = "bar"
		if foo == f:
			LOGGER.warning('\n\tFAILED TEST XX00')
			return False
		if foo != "baz":
			LOGGER.warning('\n\tFAILED TEST XX01')
			return False
		return True
	except Error as e:
		LOGGER.warning('\n\tFAILED TEST XX99')
		return False

def tests():
	#TODO: test ./ ../ ../file.txt ./file.txt etc.
	mod         = "xxx.py" #module
	ts          = [
				test_XXX(),
	]
	T = Tests(ts, mod)
	#T.pprint(**{'isQuite':True})
	T.pprint()

if __name__ == "__main__":
	tests()


