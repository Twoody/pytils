#!/usr/bin/env python3
from config import HOME
'''
Author:
	Tanner.L.Woody@gmail.com
Date:
	2019-04-01
Purpose:	
	Python os.path module does not accurately notate the ~ as a form of the path;
	This function is meant to use the HOME var in config.py to accurately fix
	 this issue when doing path checks;
'''
def set_home(s):
	l = list(s)
	ln = len(l)
	if l[0] == "~":
		if ln>1 and l[1] == '/':
			l = l[2:]
		else:
			l = l[1:]
		s = ''.join(l)
		s = HOME + '/' + s
	if s[len(s)-1] == '/':
		s = ''.join(list(s)[:len(s)-1])
	return s


