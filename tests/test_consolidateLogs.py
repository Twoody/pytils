#!/usr/bin/env python3
from pytils.config import *
from pytils.tests.Tests import Tests
from pytils.src.clean_attic import clean_attic
from pytils.src.consolidate_logs import consolidate_logs
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

	fs = [f1,f2,f3] #[f]iles
	ss = [s1,s2,s3] #[s]trings
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
	suc = clean_attic(d) #clean_attic is more `rm -rf`
	if suc == False:
		if FLAGS['isQuite'] == False and FLAGS['isVerbose'] == True:
			LOGGER.critical('\n\t\tFAILED TEST 1\n\t\tCLEAN_ATTIC:\t`%s`', suc)
		ret = True
	
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
