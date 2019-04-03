#!/usr/bin/env python3
from pytils.config import *
def has_attic():
	''' True if ~/.attic/; Else False'''
	if os.path.isdir(ATTIC):
		return True
	if os.path.isfile(ATTIC):
		if FLAGS['isQuite'] == False:
			LOGGER.warning('\n\tpytils expects '+ATTIC+' to be directory;\n\t~/.attic is file instead;')
	return False
