#!/usr/bin/env python3
from pytils.config import *
from pytils.tests.Tests import Tests
from pytils.src.clean_attic import clean_attic
'''
	THIS IS A GOOD PLACE FOR DOCUMENTATION
'''
FLAGS['isQuite'] = True

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


def consolidate_logs(d=None):
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
	if d == None:
		d = PYLOG_LOGS
	if HAS_PYLOGS == False:
		return -1
	dt  = iso()
	src = d + '/' + dt
	if os.path.isdir(src):
		if FLAGS['isQuite'] == False:
			LOGGER.warning('\n\tLOGS ALREADY CONSOLIDATED FOR DAY')
		ret = -1
	else:
		newLog = d + '/' + dt + '/consolidated.log'
		curLogs = os.listdir(d)
		os.mkdir(src)							#GET JUST LOGS BEFORE MAKING DIR
		myLogs = []
		for i in range(0, len(curLogs)):
			_log = d + "/" + curLogs[i]
			if not os.path.isfile(_log):
				continue
			myLogs.append(_log)
		myLogs = sortLogs(myLogs)
		for log in myLogs:
			hasMatch = re.search("^(.*)log(\.\d{1,2}){0,1}$", log)
			if hasMatch:
				print('good log: ' + log)
				with open(log,'r') as fh:
					all_lines = fh.readlines()
					with open(newLog, "a") as myfile:
						for line in all_lines:
					 		myfile.write(line)
				os.remove(log)
				ret +=1
			else:
				print('bad log: ' + log)
	return ret

def test_consolidate():
	d = MODULE_PATH + '/foo'
	init_testEnv(d)
	ret = True
	if consolidate_logs(d) <1:
		ret = False
	#TODO: clean up from testing...
	clean_attic(d)
	return ret

def init_testEnv(d):
	from pathlib import Path
	#TODO: Make these paths relevant to pytils package...
	s1 = 'This is the first string'
	s2 = '\tThis is a second string.'
	s3 = '\t\tAll done with a third string.'
	f1 = d + '/x.log'
	f2 = d + '/y.log'
	f3 = d + '/z.log'
	dest = d + '/logs/'
	if not os.path.exists(d+'/foo'):
		os.mkdir(d)
	Path(f1).touch()
	Path(f2).touch()
	Path(f3).touch()
	suc = consolidate_logs(d)	#Will make a d(ate)t(ime) dir we can verify in `d`;
	Path(d+"/IS_SAFE_TO_DELETE.txt").touch()
	return True
def tests():
	#TODO: test ./ ../ ../file.txt ./file.txt etc.
	mod         = "xxx.py" #module
	ts          = [
				test_consolidate(),
	]
	T = Tests(ts, mod)
	T.pprint(**{'isQuite':True})
	#T.pprint()

if __name__ == "__main__":
	tests()
