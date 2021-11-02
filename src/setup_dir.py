#!/usr/bin/env python3
from config import *
def setup_dir(d):
	''' Setup ~/.attic/ directory based on user input'''
	#TODO: Recursion?
	isWorking = ''
	if isForced:
		isWorking = 'y'
	while isWorking not in YESSES and isWorking not in NOS:
		if isWorking != "":
			print('User input not understood; Please type yes/no response;')
		isWorking = input("pytils needs to make a directory at "+d+"\nDo you wish to continue with this?")
		isWorking = isWorking.lower()
	if isWorking in NOS:
		return False
	os.mkdir(d)
	return True


