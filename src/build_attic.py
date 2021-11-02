#!/usr/bin/env python3
from config import *
def build_attic(s, **kwargs):
	'''
		Build attic directory around s(ource);
	'''
	sParentDirs = get_paths_parents(s) 	#Make a list of parent directorie
	cnt = 0
	if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
		LOGGER.info('\n\tSOURCE22:\t`%s`', s)
	for d in sParentDirs:
		dAttic = ATTIC + '/' + d
		if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
			LOGGER.info('\n\t\tSOURCE34:\t`%s`', d)
		if os.path.isfile(dAttic):
			LOGGER.critical('\n\t\tATTEMPTED attic\'ing BLOCKED BY BAD FILE:\n\t\t\t%s', dAttic)
		elif not os.path.isdir(dAttic):
			os.mkdir(dAttic)
			if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
				LOGGER.info('\n\t\tMAKING DIR: `%s`', dAttic)
			cnt+=1
		else:
			pass
	return cnt
