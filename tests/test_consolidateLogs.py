#!/usr/bin/env python3
from pytils.config import *
from pytils.tests.Tests import Tests
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


def consolidate_logs():
	import re
	ret = 0
	if HAS_PYLOGS == False:
		return -1
	dt  = iso()
	src = PYLOG_LOGS + '/' + dt
	if os.path.isdir(src):
		if FLAGS['isQuite'] == False:
			LOGGER.warning('\n\tLOGS ALREADY CONSOLIDATED FOR DAY')
		ret = -1
	else:
		newLog = PYLOG_LOGS + '/' + dt + '.log'
		curLogs = os.listdir(PYLOG_LOGS)
		os.mkdir(src)							#GET JUST LOGS BEFORE MAKING DIR
		#curLogs.sort(key=int)
		myLogs = []
		for i in range(0, len(curLogs)):
			_log = PYLOG_LOGS + "/" + curLogs[i]
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
					with open(src+'/'+dt+'.log', "a") as myfile:
						for line in all_lines:
					 		myfile.write(line)
				os.remove(log)
				ret +=1
			else:
				print('bad log: ' + log)
	return ret


def test_consolidate():
	if consolidate_logs() >0:
		return True
	return False

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
