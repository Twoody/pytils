#!/usr/bin/env python3
from pytils.config import *
from pytils.src.get_abs_path import get_abs_path
from pytils.src.has_attic import has_attic
from pytils.src.setup_dir import setup_dir
from pytils.src.build_attic import build_attic
from pytils.src.populate_attic import populate_attic
def attic(s, **kwargs):

	OFLAGS={}									#GOING TO REVERT BACK TO DEFAULT AT END;
	if kwargs is not None:
		for key, value in kwargs.items():
			if key in FLAGS:
				OFLAGS[key] = FLAGS[key]
				FLAGS[key] = value
	abspath = get_abs_path(s) 				#Get absolute path
	cnt     = 0									#Total Files saved to .attic/
	if FLAGS['isQuite'] == False:
		LOGGER.info('\n\t**** **** **** **** ATTIC PROCESS BEGINING **** **** **** ****')

	if abspath == '':
		LOGGER.warning('\n\tBAD PATH; CANNOT ATTIC;\n\t\tPATH: `%s`', s)
		LOGGER.info('\n\t**** **** **** **** ATTIC PROCESS COMPLETE **** **** **** ****')
		return -2
	elif FLAGS['isVerbose']:
		LOGGER.info('\n\tTARGET DIR: %s', abspath)
	#Verify that ~/.attic/ exists
	if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
		LOGGER.info('\n\tVERIFYING THAT `'+ATTIC+'` EXISTS')
	if has_attic() == False:
		if os.path.isfile(ATTIC):
			LOGGER.critical('\n\tABORTING ATTIC SCRIPT; IMPROPER CONFIGURATION FOR pytils;')
			return -1
		else:
			madeAttic = setup_dir(ATTIC) #Feed Back
			if madeAttic == False:
				#User does not want us to configure their home dir; We will abort process;
				return -1
			else:
				LOGGER.info('\n\tCREATED USERS\' ATTIC DIRECTORY IN HOME DIR;')
	else:
		if FLAGS['isVerbose'] == True:
			LOGGER.info('\n\t%s: ALREADY EXISTS;', ATTIC)

	#Check size of requested `attic`
	#	If way to large, reject users request
	#	If to large, ask for user input
	#	If reasonable, no user input necessary
	
	#Verifty full ~/.attic/ + absolutePath exists
	if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
		LOGGER.info('\n\tBUILDING UP  `'+ATTIC+'` DIRECTORIES')
	atticDirs = build_attic(abspath)

	#populate attic with requested file/dir
	__s = get_abs_path(s, **{'keepAsFile':True})
	if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
		LOGGER.info(
			'\n\tPOPULATING `'+ATTIC+'` DIRECTORY\n\tCALLING ON: ' + __s
		)
	cnt += populate_attic(__s)
	if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
		LOGGER.info('\n\tPOPULATED %s ITEMS', str(cnt))

	if FLAGS['isQuite'] == False:
		LOGGER.info('\n\t**** **** **** **** ATTIC PROCESS COMPLETE **** **** **** ****')
	for key,value in OFLAGS.items():
		FLAGS[key] = value
	return cnt

