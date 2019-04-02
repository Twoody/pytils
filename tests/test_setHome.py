#!/usr/bin/env python3
from pytils.config import *
from pytils.src.set_home import set_home
from pytils.tests.Tests import Tests
'''
	THIS IS A GOOD PLACE FOR DOCUMENTATION
'''

def test_tilda():
	f = '~'
	try:
		foo = set_home(f)
		if foo == f:
			LOGGER.warning('\n\tFAILED TEST 300')
			return False
		if foo != HOME:
			LOGGER.warning('\n\tFAILED TEST 301\n\t\tFOO:\t%s\n\t\tHOME:\t%s', foo, HOME)
			return False
		return True
	except Error as e:
		LOGGER.warning('\n\tFAILED TEST 399')
		return False

def test_tilda2():
	f = '~/.pylog/'
	try:
		foo = set_home(f)
		if foo == f:
			LOGGER.warning('\n\tFAILED TEST 310')
			return False
		if foo != HOME + '/.pylog':
			LOGGER.warning('\n\tFAILED TEST 311\n\t\tFOO:\t%s\n\t\tPLOG:\t%s', foo, HOME+'/.pylog')
			return False
		return True
	except Error as e:
		LOGGER.warning('\n\tFAILED TEST 399')
		return False

def tests():
	#TODO: test ./ ../ ../file.txt ./file.txt etc.
	mod         = "set_home.py" #module
	ts          = [
				test_tilda(),
				test_tilda2(),
	]
	T = Tests(ts, mod)
	#T.pprint(**{'isQuite':True})
	T.pprint()

if __name__ == "__main__":
	tests()
