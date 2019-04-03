#!/usr/bin/env python3
from pytils.config import *
def clean_attic(s, **kwargs):
	'''
		Nuke contents; rm -rf of s(ource)
		Directory being nuked must contain a marker which is wildcard detected;
	'''
	from shutil import rmtree
	from glob import glob
	ret = True
	OFLAGS={}									#GOING TO REVERT BACK TO DEFAULT AT END;
	if kwargs is not None:
		for key, value in kwargs.items():
			if key in FLAGS:
				OFLAGS[key] = FLAGS[key]
				FLAGS[key] = value
	if os.path.isfile(s):
		if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
			LOGGER.info('\n\t\tREMOVING FILE:\t%s', s)
		os.remove(s)
	elif os.path.isdir(s):
		is_safe = glob( ATTIC + s + '/IS_SAFE_TO_DELETE.txt*')		#Note wildcard appendage
		if len(is_safe) > 0 and not os.path.isfile(is_safe[0]):
			LOGGER.warning('Trying to remove directory which is not safe to remove...')
			ret = False
		else:
			if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
				LOGGER.info('\n\t\tREMOVING DIR:\t%s', s)
			rmtree(s)
	else:
		LOGGER.warning('\n\tUNABLE TO DETERMINE `%s`\n', s)
		ret = False
	for key,value in OFLAGS.items():
		FLAGS[key] = value
	return ret

