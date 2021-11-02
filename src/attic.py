#!/usr/bin/env python3
from config import *
from src.get_abs_path import get_abs_path
from src.has_attic import has_attic
from src.setup_dir import setup_dir
from src.build_attic import build_attic
from src.populate_attic import populate_attic
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
		LOGGER.info('\n\n\t**** **** **** **** ATTIC PROCESS BEGINING **** **** **** ****')

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
		LOGGER.info('\n\t**** **** **** **** ATTIC PROCESS COMPLETE **** **** **** ****\n\n')
	for key,value in OFLAGS.items():
		FLAGS[key] = value
	return cnt

if __name__ == "__main__":
	#Called directly, should have arguments...
	fullCmdArguments = sys.argv

	# - further arguments
	argumentList = fullCmdArguments[1:]
	reqs	= []

	# - Argument Processing
	for arg in argumentList:
		isFlag = re.search(FLAG_RE, arg)
		if isFlag:
			if arg in ("-v", "--verbose"):
				if FLAGS['isQuite'] == False:
					LOGGER.info("\n\tEnabling verbose mode")
				FLAGS['isVerbose'] = True
			elif arg in ("-h", "--help"):
				#TODO: Make a helper function O.o
				LOGGER.info("\n\tFor current help please email at Tanner.L.Woody@gmail.com")
				sys.exit(0)
			elif arg in ("-q", "--quite"):
				FLAGS['isQuite'] = True
				#LOGGER.info("\n\tOutput to stdout disabled;")
			else:
				if FLAGS['isQuite'] == False:
					LOGGER.warning("\n\tArgument not recgonized: %s" %arg)
		else:
			reqs.append(arg)

	# - Function Calls
	if len(reqs) == 0:
		LOGGER.error('\n\t/pytils/src/attic.py: No argment provided to attic')
		sys.exit(0)
	elif len(reqs) == 1:
		attic(reqs[0])
		#LOGGER.info('\n\tTEST CALLS:\n\t%s',reqs[0])
	else:	
		msg = '\n\t/pytils/src/attic.py: TOO MANY ARGUMENTS:'
		for arg in reqs:
			msg += '\n\t\tARG:\t%s'%arg
		LOGGER.error(msg)
		sys.exit(0)
