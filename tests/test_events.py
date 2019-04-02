'''
WARNING:
	THIS IS CURRENTLY ONLY AN EXAMPLE AND WILL NOT RUN;
	THIS IS MEANT TO DEMONSTRATE HOW TO APPROPRIATELY PUT TOGETHER
	 CLASSES AND TESTS INTO A SINGLE FRAMEROWKR
'''

import sys
sys.path.append('/Users/tannerleewoody/Workspace/pydir/life/src/')
from Events import *

def test_import():
	E = Events()
	if not E:
		return False
	return True

def test_version():
	E = Events({'isquite':True})
	try:
		E.printVersion()
		return True
	except:
		return False
def test_getTables():
	E = Events({'isquite':True})
	tables = E.getTables()
	fEvents = False
	if tables == []:
		print("\tWARNING: " + E.thisFile + ": DB `"+E.dbPath+"` IS EMPTY")
		return False
	for tObj in tables:
		table = tObj[0]
		if table == "events":
			fEvents = True
	if fEvents == False:
		print("\tWARNING: " + E.thisFile + ": COULD NOT FIND TABLE `events`")
		return False
	return True
def test_getSchema(tName):
	E      = Events({'isquite':True})
	schema = E.getSchema(tName)
	if schema == []:
		print("\tWARNING: " + E.thisFile + ": FAILED FETCHING SCHEMA FOR TABLE events")
		return False
	return True
def test_getColumns(tName):
	E       = Events({'isquite':True})
	search  = 'url' #This should be a column name...
	columns = E.getColumns(tName)
	if columns == []:
		print("\tWARNING: " + E.thisFile + ": FAILED FETCHING COLUMNS FOR TABLE " + tName)
		return False
	if search not in columns:
		print("\tWARNING: " + E.thisFile + ": FAILED FETCHING COLUMN "+search+" FROM TABLE " + tName)
		return False
	return True
def test_insert(tName, toInsert):
	E       = Events({'isquite':True})
	columns = E.getColumns(tName)
	values  = [toInsert]*len(columns)
	E.insert(tName, values)
	return True
def test_getSize(tName):
	E       = Events({'isquite':True})
	size    = E.getSize(tName)
	if size <= 0: #Should be at least 1
		print("\tWARNING: " + E.thisFile + ": COULD NOT COUNT FROM " + tName)
		print('\t\tRETURNED COUNT FROM ' + E.thisFile + '.getSize(): ' + str(size))
		return False
	return True
def test_pprint(tName, toPrint):
	E      = Events({'isquite':True})
	select = 'event = "' + toPrint + '"'
	events = E.getEvent(tName, select)
	event  = events[0]
	event.pprint({'isQuite':True}) #Return the string rather than print
	return True
	
def test_delete(tName, whereClause, toDelete):
	E = Events({'isquite':True})
	E.delete(tName, whereClause, toDelete)
	return True
def tests():
	from tests import Tests
	testTable   = "events"
	testInsert  = "testItem"
	deleteWhere = "event = ?"
	mod         = "Events.py" #module
	ts          = [
				test_import(), 
				test_version(), 
				test_getTables(), 
				test_getSchema(testTable), 
				test_getColumns(testTable), 
				test_insert(testTable, testInsert),
				test_getSize(testTable), 
				test_pprint(testTable, testInsert),
				test_delete(testTable, deleteWhere, testInsert)
	]
	T = Tests(ts, mod)
	T.pprint()
