#!/usr/bin/env python3
import os
import sys
import sqlite3
import logging
import re
from logging.config import fileConfig
from datetime import datetime
from shutil import copyfile
from glob import glob

#GENERAL GLOBAL VARIABLES
ISO_RE = r'^(.*)(T)(.*)$'
LOG_RE = r'^(.*)log(\.\d{1,2}){0,1}$'

THIS_FILE=os.path.realpath( __file__ )
HOME=os.path.expanduser("~")
ATTIC=HOME + '/.attic'
MODULE_PATH=os.path.dirname(THIS_FILE)
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

def iso(*args):
	#TDOD: Arguments for just YYYY-M-D or HH:MM
	#		Could just have an hasYear, hasMonth, ...
	if args is None or args==():
		args = {}
	else:
		args = args[0]
	ret = datetime.isoformat(datetime.now())
	if 'dateOnly' in args and args['dateOnly'] == True:
		ret = re.sub(ISO_RE, r'\1', ret)
	elif 'timeOnly' in args and args['dateOnly'] == True:
		ret = re.sub(ISO_RE, r'\2', ret)
	return ret
def get_paths_parents(s):
	''' Get each path of source '''
	ret = []
	while s != "/":
		ret.append(s)
		s = os.path.dirname(s)
	ret.reverse()	#Want shortest path first
	return ret
