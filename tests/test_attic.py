#!/usr/bin/env python3
from pytils.config import *
from pytils.tests.Tests import Tests
from pytils.src.get_abs_path import get_abs_path
from glob import glob
from pytils.src.clean_attic import clean_attic
'''
	THIS IS A GOOD PLACE FOR DOCUMENTATION
'''
def hasAttic():
	''' True if ~/.attic/; Else False'''
	if os.path.isdir(ATTIC):
		return True
	if os.path.isfile(ATTIC):
		if FLAGS['isQuite'] == False:
			LOGGER.warning('\n\tpytils expects '+ATTIC+' to be directory;\n\t~/.attic is file instead;')
	return False

def setup_dir(d):
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

def get_paths_parents(s):
	''' Get each path of source '''
	ret = []
	while s != "/":
		ret.append(s)
		s = os.path.dirname(s)
	ret.reverse()	#Want shortest path first
	return ret

def buildAttic(s, **kwargs):
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

def populateAttic(s, **kwargs):
	'''
	Populate ~/.attic/ with all items from s(ource);
		If s is dir, recurse through for all content 
		If s is file, populate single item;
	'''
	dt  = iso()
	cnt = 0
	if os.path.isfile(s):
		file_to_attic = ATTIC + '/' + s + '.' + dt
		if not os.path.isdir(ATTIC + "/" + os.path.dirname(s)):
			if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
				LOGGER.info('\n\tBUILDING ATTIC ON:\t%s', s)
			buildAttic(s)
		if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
			LOGGER.info('\n\tATTEMPTING ARCHIVE:\n\t\tSRC:\t%s\n\t\tDEST:\t%s', s, file_to_attic)
		copyfile(s, file_to_attic)
		if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
			LOGGER.info('\n\tARCHIVED `%s`', s)
		cnt += 1
	elif os.path.isdir(s):
		if not os.path.isdir(ATTIC + "/" +s):
			buildAttic(s)
		if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
			LOGGER.info('\n\tARCHIVING DIR `%s`', s)
		content = os.listdir(s)
		for item in content:
			cnt += populateAttic(s+'/'+item)
	else:
		LOGGER.critical('\n\tCRAZY MALFUNCTION WITH `%s`', s)
	return cnt

def attic(s, **kwargs):
	from pytils.config import FLAGS
	from pytils.src.get_abs_path import get_abs_path

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
	if hasAttic() == False:
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
	atticDirs = buildAttic(abspath)

	#populate attic with requested file/dir
	__s = get_abs_path(s, **{'keepAsFile':True})
	if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
		LOGGER.info(
			'\n\tPOPULATING `'+ATTIC+'` DIRECTORY\n\tCALLING ON: ' + __s
		)
	cnt += populateAttic(__s)
	if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
		LOGGER.info('\n\tPOPULATED %s ITEMS', str(cnt))

	if FLAGS['isQuite'] == False:
		LOGGER.info('\n\t**** **** **** **** ATTIC PROCESS COMPLETE **** **** **** ****')
	for key,value in OFLAGS.items():
		FLAGS[key] = value
	return cnt

def test_file():
	#TODO: Move below file to pytils package
	f   = '~/Workspace/resources/files_for_testing/foo.temp'
	ret = True
	foo = attic(f, **{'isQuite':True})
	src = ATTIC + get_abs_path(f)
	if foo <1:
		if FLAGS['isQuite'] == False:
			if FALGS['isVerbose'] == True:
				LOGGER.info('\n\tFOO:\t%s', str(foo))
			LOGGER.warning('\n\tFAILED TEST 400')
		ret = False
	else:
		didWork = clean_attic(src)
		if not didWork:
			LOGGER.warning('\n\ttest file never deleted from attic')
			ret = False
		elif FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
			LOGGER.info('\n\tTEST_FILE: PEMANENTLY REMOVED:\n\t\t%s', src)
	return ret

def test_dir1():
	#make file and dir; test; remove test files and dirs;
	#For verbosity, uncomment line below
	#FLAGS['isVerbose'] = True
	init_testEnv()
	ret = True
	d = '~/Workspace'
	d = get_abs_path(d)
	f1 = d + '/foo/x.temp'
	attic(d+'/foo/', **{'isQuite':True})
	src1 = ATTIC + f1 + '*'
	src2 = ATTIC + d + '/foo/'
	globs  = glob(src1)
	if len(globs) < 1:
		LOGGER.warning('\n\tFAILED TEST 410.a\n\t\tSRC:\t%s', src1)
	elif not os.path.isfile(globs[0]):
		LOGGER.warning('\n\tFAILED TEST 410.b')
		ret = False
	else:
		if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
			LOGGER.info('\n\tFOUND SRC TO REMOVE FROM ATTIC\n\t\tSOURCE:\t%s', src1)
		didWork = clean_attic(src2)
		if didWork == False:
			LOGGER.warning('\n\tATTIC NOT CLEANED OUT\n\t\tSRC:\t%s', src2)
			ret = False
		else:
			if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
				LOGGER.info('\n\tCLEANED OUT DIRECTORY\n\t\tSRC:\t%s',src2)
			
	if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
		LOGGER.info('\n\tNuking ATTIC\n\t\tSOURCE:\t%s', d+'/foo/')
	didWork = clean_attic(d+'/foo/')
	if didWork == False:
		LOGGER.warning('\n\tWORK DIRECTORY NOT CLEANED OUT')

	return ret

def test_dir2():
	#make file and dir; test; remove test files and dirs;
	init_testEnv()
	ret = True
	d = '~/Workspace'
	d = get_abs_path(d)
	f1 = d + '/foo/bar/y.temp'
	#attic(d+'/foo/')
	attic(d+'/foo/', **{'isQuite':True})

	src1 = ATTIC + f1 + '*'
	src2 = ATTIC + d + '/foo/'
	globs  = glob(src1)
	if len(globs) < 1:
		LOGGER.warning('\n\tFAILED TEST 411.a\n\t\tSRC:\t%s', src1)
	elif not os.path.isfile(globs[0]):
		LOGGER.warning('\n\tFAILED TEST 411.b')
		ret = False
	else:
		if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
			LOGGER.info('\n\tFOUND SRC TO REMOVE FROM ATTIC\n\t\tSOURCE:\t%s', src1)
		didWork = clean_attic(src2)
		if didWork == False:
			LOGGER.warning('\n\tATTIC NOT CLEANED OUT\n\t\tSRC:\t%s', src2)
			ret = False
		else:
			if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
				LOGGER.info('\n\tCLEANED OUT DIRECTORY\n\t\tSRC:\t%s',src2)
	return ret



	if not os.path.isfile(ATTIC +  '/' + f2):
		LOGGER.warning('\n\tFAILED TEST 412')
		ret = False
	clean_attic(d+'/foo/')
	return ret

def test_dir3():
	#make file and dir; test; remove test files and dirs;
	init_testEnv()
	ret = True
	d = '~/Workspace'
	d = get_abs_path(d)
	f3 = d + '/foo/bar/bazz.temp'
	#attic(d+'/foo/')
	attic(d+'/foo/', **{'isQuite':True})
	if not os.path.isfile(ATTIC +  '/' + f3):
		LOGGER.warning('\n\tFAILED TEST 413')
		ret = False
	clean_attic(d+'/foo/')
	return ret

def test_dir4():
	#make file and dir; test; remove test files and dirs;
	init_testEnv()
	ret = True
	d = '~/Workspace'
	d = get_abs_path(d)
	f1 = d + '/foo/x.temp'
	f2 = d + '/foo/bar/y.temp'
	f3 = d + '/foo/bar/baz/z.temp'
	#attic(d+'/foo/')
	attic(d+'/foo/', **{'isQuite':True})
	if not os.path.isfile(ATTIC +  '/' + f1):
		LOGGER.warning('\n\tFAILED TEST 420')
		ret = False
	if not os.path.isfile(ATTIC +  '/' + f2):
		LOGGER.warning('\n\tFAILED TEST 421')
		ret = False
	if not os.path.isfile(ATTIC +  '/' + f3):
		LOGGER.warning('\n\tFAILED TEST 422')
		ret = False
	clean_attic(d+'/foo/')
	return ret

def init_testEnv():
	from pathlib import Path
	#TODO: Make these paths relevant to pytils package...
	d = '~/Workspace'
	d = get_abs_path(d)
	f1 = d + '/foo/x.temp'
	f2 = d + '/foo/bar/y.temp'
	f3 = d + '/foo/bar/baz/z.temp'
	if not os.path.exists(d+'/foo'):
		os.mkdir(d+'/foo')
	if not os.path.exists(d+'/foo/bar'):
		os.mkdir(d+'/foo/bar')
	if not os.path.exists(d+'/foo/bar/baz'):
		os.mkdir(d+'/foo/bar/baz/')
	Path(f1).touch()
	Path(f2).touch()
	Path(f3).touch()
	Path(d+"/foo/IS_SAFE_TO_DELETE.txt").touch()
	return True

def tests():
	#TODO: test ./ ../ ../file.txt ./file.txt etc.
	mod         = "attic.py" #module
	ts          = [
				test_file(),
				test_dir1(),
				test_dir2(),
			#	test_dir3(),
			#	test_dir4(),
	]
	T = Tests(ts, mod)
	#T.pprint(**{'isQuite':True})
	T.pprint()

if __name__ == "__main__":
	tests()

