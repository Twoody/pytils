from pytils.config import *
def test_logger():
	try:
		x = LOGGER.debug('Just a test')
		return True
	except Error as e:
		return False
def test_home():
	try:
		if (type(HOME) == str):
			return True
		return False
	except Error as e:
		return False


def tests():
	#from tests import Tests
	from pytils.tests.Tests import Tests
	mod         = "__init__.py" #module
	ts          = [
				test_logger(),
				test_home(),
				#test_iso1, 				#TODO: Test `dateOnly`
				#test_iso2, 				#TODO: Test `timeOnly`
				#test_getPathsParent, 	#TODO: Test on /pytils/ dirs with test env.
	]
	T = Tests(ts, mod)
	T.pprint()

if __name__ == "__main__":
	tests()
