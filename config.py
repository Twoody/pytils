#!/usr/bin/env python3
import os
import sys
import sqlite3
import logging
from logging.config import fileConfig
from datetime import datetime
from shutil import copyfile
from glob import glob

THIS_FILE=os.path.realpath( __file__ )
HOME=os.path.expanduser("~")
ATTIC=HOME + '/.attic'
#sys.path.append( HOME + '/utils/python/' )

#Logger to log to path defined in ~/.pylog/config.ini
PYLOG=HOME + '/.pylog' 
PYLOG_CONFIG=PYLOG + '/config.ini'
PYLOG_LOGS=PYLOG + '/logs'
fileConfig(PYLOG_CONFIG)
LOGGER=logging.getLogger(THIS_FILE)
HAS_PYLOGS=True if os.path.isfile(PYLOG_CONFIG) else False
FLAGS={
	'isQuite':False,
	'isLogging':True,
	'isDebug':False,
	'isStdO':False,
	'isVerbose':False
}
YESSES=[
	'y',
	'si',
	'ok',
	'ya',
	'ja',
	'yes',
	'eys',
	'oui',
	'okay',
	'sure',
	'no problem',
]
NOS=[
	'n',
	'no',
	'non',
	'nein',
	'no thank you',
	'no thanks',
]

def iso():
	#TDOD: Arguments for just YYYY-M-D or HH:MM
	#		Could just have an hasYear, hasMonth, ...
	ret = datetime.isoformat(datetime.now())
	return ret
def get_paths_parents(s):
	''' Get each path of source '''
	ret = []
	while s != "/":
		ret.append(s)
		s = os.path.dirname(s)
	ret.reverse()	#Want shortest path first
	return ret
