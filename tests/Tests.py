from pytils.config import *


class Tests:
	def __init__(self, tests, module):
		self.module  = module
		self.tests   = tests
		self.total   = len(tests)
		self.success = self.getSuccesses()
	def getSuccesses(self):
		suc = 0
		for t in self.tests:
			if t:
				suc += 1
		return suc
	def pprint(self, **kwargs):
		if kwargs is not None:
			for key, value in kwargs.items():
				if key in FLAGS:
					FLAGS[key] = value
		if FLAGS['isLogging'] == False and FLAGS['isStdO'] == False:
			isQuite = True
		s = "\n\t**************************************************************************\n"
		s += "\t" + self.module +":\n"
		s += "\t\tPASSED " + str(self.success) + " OF " + str(self.total) + " TESTS\n"
		s += "\t**************************************************************************\n\n"
		if FLAGS['isQuite'] == False:
			if FLAGS['isStdO'] == True:
				print(s)
			elif FLAGS['isLogging'] == True:
				LOGGER.info(s)	#TODO: Make flag for no logging and no printing;
		return True

if __name__ == "__main__":
	import test_imports
	import test_getAbsPath
	import test_setHome
	import test_attic
	test_imports.tests()
	test_setHome.tests()
	test_getAbsPath.tests()
	test_attic.tests()
