#!/usr/bin/env python3
from pytils.config import *
from pytils.src.build_attic import build_attic
def populate_attic(s, **kwargs):
	'''
	Populate ~/.attic/ with all items from s(ource);
		If s is dir, recurse through for all content 
		If s is file, populate single item;
	'''
	#TODO: Arg for milliseconds to be turned off
	dt   = iso()
	dt	  = dt.replace('-','')
	dt	  = dt.replace(':','-')
	date = re.sub(ISO_RE, r'\1', dt)
	time = re.sub(ISO_RE, r'\3', dt)
	dt	  = dt.replace('T','_')

	cnt  = 0
	if os.path.isfile(s):
		file_to_attic = ATTIC + '/' + s + '.' + dt
		if not os.path.isdir(ATTIC + "/" + os.path.dirname(s)):
			if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
				LOGGER.info('\n\tBUILDING ATTIC ON:\t%s', s)
			build_attic(s)
		if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
			LOGGER.info('\n\tATTEMPTING ARCHIVE:\n\t\tSRC:\t%s\n\t\tDEST:\t%s', s, file_to_attic)
		copyfile(s, file_to_attic)
		if FLAGS['isQuite'] == False:
			LOGGER.info('\n\tARCHIVED\n\t\tSRC:\t%s\n\t\tDEST:\t%s', s, file_to_attic)
		cnt += 1
	elif os.path.isdir(s):
		if not os.path.isdir(ATTIC + "/" +s):
			build_attic(s)
		if FLAGS['isQuite'] == False:
			LOGGER.info('\n\tARCHIVING DIR `%s`', s)
		content = os.listdir(s)
		for item in content:
			cnt += populate_attic(s+'/'+item)
	else:
		LOGGER.critical('\n\tCRAZY MALFUNCTION WITH `%s`', s)
	return cnt


