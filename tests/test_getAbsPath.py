#!/usr/bin/env python3
from config import *
from src.get_abs_path import get_abs_path
from tests.Tests import Tests
'''
	THIS IS A GOOD PLACE FOR DOCUMENTATION
'''

def test_getPath():
	f = 'just_a_string.txt'
	try:
		foo = get_abs_path(f, **{'isQuite':True})
		return True
	except Error as e:
		LOGGER.warning('\n\tFAILED TEST 200')
		return False

def test_badpath1():
	bp = '/FAKE_FILE.TRASH'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		return True

	bp = './FAKE_FILE.TRASH'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		return True

	bp = 'FAKE_FILE.TRASH'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		return True

	bp = '/Users/FAKE_FILE.TRASH'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		return True

	LOGGER.warning('\n\tFAILED TEST 209')
	return False
def test_badpath2():
	bp = '/FAKE_DIR'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		return True

	bp = '/FAKE_DIR/'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		return True

	bp = '~/FAKE_DIR'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		return True

	bp = 'FAKE_DIR'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		return True

	LOGGER.warning('\n\tFAILED TEST 219')
	return False

def test_goodpath1():
	bp = '~/.pylog/README.txt'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		LOGGER.warning('\n\tFAILED TEST 228')
		return False

	bp = 'tests/Tests.py'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		LOGGER.warning('\n\tFAILED TEST 227')
		return False

	bp = '/Users/tannerleewoody/.pylog/README.txt'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		LOGGER.warning('\n\tFAILED TEST 226')
		return False

	bp = HOME + '/.pylog/README.txt'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		LOGGER.warning('\n\tFAILED TEST 225')
		return False

	return True
def test_goodpath2():
	bp = '~/.pylog/'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		LOGGER.warning('\n\tFAILED TEST 231')
		return False

	bp = './tests/'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		LOGGER.warning('\n\tFAILED TEST 232')
		return False

	bp = '/Users/tannerleewoody/.pylog/'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		LOGGER.warning('\n\tFAILED TEST 233')
		return False

	bp = HOME + '/.pylog/README.txt'
	if get_abs_path(bp, **{'isQuite':True}) == "":
		LOGGER.warning('\n\tFAILED TEST 235')
		return False

	return True

def tests():
	#TODO: test ./ ../ ../file.txt ./file.txt etc.
	mod         = "get_abs_path.py" #module
	ts          = [
				test_getPath(),
				test_badpath1(),
				test_badpath2(),
				test_goodpath1(),
				test_goodpath2(),
	]
	T = Tests(ts, mod)
	#T.pprint(**{'isQuite':True})
	T.pprint()

if __name__ == "__main__":
	tests()
