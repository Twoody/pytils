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
				test_home()
	]
	T = Tests(ts, mod)
	T.pprint()

if __name__ == "__main__":
	tests()
