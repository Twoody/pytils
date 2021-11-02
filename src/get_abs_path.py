#!/usr/bin/env python3
from config import *
from src.set_home import set_home
'''
Author:
	Tanner.L.Woody@gmail.com
Date:
	2019-04-01
Purpose:	
	Always return the absolute path of a file, homedir, etc.
	Return emptry string if file/dir not found;

'''

def get_abs_path(s, **kwargs):
	OFLAGS={}							#GOING TO REVERT BACK TO DEFAULT AT END;
	args = {}
	if kwargs is not None:
		for key, value in kwargs.items():
			if key in FLAGS:
				OFLAGS[key] = FLAGS[key]
				FLAGS[key] = value
			else:
				args[key] = value
	ret = ''
	s = set_home(s)
	if os.path.isfile(s):
		if 'keepAsFile' in args and args['keepAsFile'] == True:
			ret = os.path.abspath(s)
		else:
			ret = os.path.dirname(os.path.abspath(s))
	elif os.path.isdir(s):
		ret = os.path.abspath(s)
	elif FLAGS['isQuite'] == False:
		if FLAGS['isVerbose'] == True:
			LOGGER.warning('\n\tUNKNOWN FORMAT BEING SEARCHED; No path determined')
		else:
			LOGGER.debug('\n\tUNKNOWN FORMAT BEING SEARCHED; No path determined')
	else:
		#isQuite == True; Stay quite...
		pass
	if FLAGS['isVerbose']:
		LOGGER.debug('\n\tget_abs_path.py: PATH: `%s`', ret)
	for key,value in OFLAGS.items():
		FLAGS[key] = value
	return ret

