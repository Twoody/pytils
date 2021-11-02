#!/usr/bin/env python3
from config import *
from tests.Tests import Tests
from src.get_abs_path import get_abs_path
from src.clean_attic import clean_attic
from src.attic import attic
'''
	THIS IS A GOOD PLACE FOR DOCUMENTATION
'''

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
	if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
		LOGGER.info('\n\tNuking ATTIC\n\t\tSOURCE:\t%s', d+'/foo/')
	didWork = clean_attic(d+'/foo/')
	if didWork == False:
		LOGGER.warning('\n\tWORK DIRECTORY NOT CLEANED OUT')
	return ret

def test_dir3():
	#make file and dir; test; remove test files and dirs;
	init_testEnv()
	ret     = True
	d       = '~/Workspace'
	d       = get_abs_path(d)
	f1      = d + '/foo/bar/baz/z.temp'
	didWork = attic(d+'/foo', **{'isQuite':True})
	src1    = ATTIC + f1 + '*'
	src2    = ATTIC + d + '/foo'
	globs   = glob(src1)
	if didWork < 1:
		if FLAGS['isQuite'] == False:
			LOGGER.warning('\n\tattic.py: FAILED TO ATTIC:\n\t\t%s', f1)
			return False
	if len(globs) < 1:
		LOGGER.warning('\n\tFAILED TEST 413.a\n\t\tSRC:\t%s', src1)
		ret = False
	elif not os.path.isfile(globs[0]):
		LOGGER.warning('\n\tFAILED TEST 413.b')
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
	didWork = clean_attic(d+'/foo')
	if didWork == False:
		LOGGER.warning('\n\tWORK DIRECTORY NOT CLEANED OUT')
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
				test_dir3(),
			#	test_dir4(),
	]
	T = Tests(ts, mod)
	#T.pprint(**{'isQuite':True})
	T.pprint()

if __name__ == "__main__":
	tests()

