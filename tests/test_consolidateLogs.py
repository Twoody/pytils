#!/usr/bin/env python3
from pytils.config import *
from pytils.tests.Tests import Tests
from pytils.src.clean_attic import clean_attic
from pytils.src.attic import attic
'''
	THIS IS A GOOD PLACE FOR DOCUMENTATION
'''
def init_testEnv(d):
	from pathlib import Path
	#TODO: Make these paths relevant to pytils package...
	s1 = 'This is the first string\n'
	s2 = '\tThis is a second string.\n'
	s3 = '\t\tAll done with a third string.\n'
	f1 = d + '/x.log'
	f2 = d + '/y.log'
	f3 = d + '/z.log'

	fs = [f1,f2,f3]
	ss = [s1,s2,s3]
	#TODO: dest support
	dest = d + '/logs/'
	if not os.path.exists(d):
		os.mkdir(d)
	for i in range(0, len(fs)):
		Path(fs[i]).touch()
		with open(fs[i],'w') as fh:
			fh.write(ss[i])
		#attic(fs[i]) #Verifying path works by copying to ~/.attiic/
	Path(d+"/IS_SAFE_TO_DELETE.txt").touch()
	return True


def sortLogs(logs):
	''' Logs are strings stored from 1-20;
	Logs also have top level log with no extension;
	Test log for extenstion would be nice..
	We can also just do when the file was last modified, as files should be read only...
	'''
	import operator
	dic = {}
	for log in logs:
		dic[str(log)] = os.path.getmtime(log)
	dic = sorted(dic.items(), key=operator.itemgetter(1))
	ret = []
	for t in dic:
		ret.append(t[0])
	return ret 


def consolidate_logs(d=None, **kwargs):
	import re
	'''Consolidate pylogs into one file.
	File should be d(ate) and t(ime) stamped;
	Remove all logs that we consolidated and start new.
	'''
	#TODO:
	#	1. Structure appropriately:
	#			make /archive/ dir;
	#			make /archive/yyyy-mm-dd/ dirs
	#			make /archive/yyyy-mm-dd/HHHH-MM.log files
	#	2. Take in parameters and flags
	#			-f(orce) for consolidating more than just pylogs
	#			-t(arget) for target destination file
	#			/dir/ param instead of 	PYLOG_LOGS
	#			`newLog` to be dynamic
	#			regex param for when we call `sortLogs`
	ret = 0
	if d is None:
		d = PYLOG_LOGS
	if HAS_PYLOGS == False:
		return -1

	OFLAGS={}									#GOING TO REVERT BACK TO DEFAULT AT END;
	if kwargs is not None:
		for key, value in kwargs.items():
			if key in FLAGS:
				OFLAGS[key] = FLAGS[key]
				FLAGS[key] = value
	dt   = iso()
	dt	  = dt.replace('-','')
	dt	  = dt.replace(':','-')
	date = re.sub(ISO_RE, r'\1', dt)
	time = re.sub(ISO_RE, r'\3', dt)
	dt	  = dt.replace('T','_')

	src  = d + '/' + date
	if os.path.isdir(src):
		if FLAGS['isQuite'] == False:
			LOGGER.warning('\n\tLOGS ALREADY CONSOLIDATED FOR DAY')

	newLog  = src + '/' + time + '.consolidated.log'
	curLogs = os.listdir(d)
	myLogs  = []
	if FLAGS['isQuite'] == False:
		LOGGER.info('\n\tMAKING DIRECTORY:\n\t\t%s', src)
	if os.path.isdir(src):
		if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
			LOGGER.critical('\n\tMSG 4873: DIRECTORY ALREADY EXISTS:\n\t\t%s', src)
	elif os.path.isfile(src):
		if FLAGS['isQuite'] == False:
			LOGGER.critical('\n\tpytils NEEDS TO MAKE DIR WHERE FILE IS LOCATED:\n\t\t%s', src)
		#TODO: Handle the copy-pasta below better...
		for key,value in OFLAGS.items():
			FLAGS[key] = value
		return -1
	else:
		os.mkdir(src)							#GET JUST LOGS BEFORE MAKING DIR
	for i in range(0, len(curLogs)):
		_log = d + "/" + curLogs[i]
		if not os.path.isfile(_log):
			continue
		myLogs.append(_log)

	myLogs = sortLogs(myLogs)
	for log in myLogs:
		hasMatch = re.search(LOG_RE, log)
		if hasMatch:
			if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
				LOGGER.info('\n\tgood log:%s\t', log)
			with open(log,'r') as fh:
				all_lines = fh.readlines()
				with open(newLog, "a") as myfile:
					for line in all_lines:
				 		myfile.write(line)
					if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
						LOGGER.info('\n\tWROTE TO:\n\t\t%s', myfile)
			if FLAGS['isQuite'] == False:
				LOGGER.info('\n\tCONSOLIDATED LOG:\n\t\t%s\n\tREMOVING OLD LOG:\n\t\t%s', newLog, log)
			#TODO: -p(reserve) logs flag...
			os.remove(log)
			ret += 1
		else:
			if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
				LOGGER.info('\n\tbad log:%s\t', log)
	#TODO: Handle the copy-pasta below better...
	for key,value in OFLAGS.items():
		FLAGS[key] = value
	return ret

def test_consolidate():
	d = MODULE_PATH + '/foo'
	init_testEnv(d)
	ret = True
	cons = consolidate_logs(d, **{'isQuite':True})
	if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
		LOGGER.info('\n\t**** **** TEST ONE **** ****')
	if  cons <1:
		ret = False
		if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
			LOGGER.critical('\n\t\tFAILED TEST 1\n\t\tCONS:\t`%s`', cons)
#	suc = clean_attic(d) #clean_attic is more `rm -rf`
#	if suc == False:
#		if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
#			LOGGER.critical('\n\t\tFAILED TEST 1\n\t\tCLEAN_ATTIC:\t`%s`', suc)
#		ret = True
	
	if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
		if ret == True:
			LOGGER.info('\n\tPASSED TEST 1')
		else:
			LOGGER.info('\n\tFAILED TEST 1')
	return ret
def tests():
	#TODO: test ./ ../ ../file.txt ./file.txt etc.
	mod         = "consolidate_logs.py" #module
	ts          = [
				test_consolidate(),
	]
	T = Tests(ts, mod)
	#T.pprint(**{'isQuite':True})
	T.pprint()

if __name__ == "__main__":
	tests()
