#!/usr/bin/env python3
import os
import sys
import sqlite3
import logging
from logging.config import fileConfig
from datetime import datetime
from shutil import copyfile

HOME = os.path.expanduser("~")
ATTIC = HOME + '/.attic'
#sys.path.append( HOME + '/utils/python/' )

#Logger to log to path defined in ~/.pylog/config.ini
fileConfig( HOME + '/.pylog/config.ini' )
FILE=os.path.realpath( __file__ )
LOGGER=logging.getLogger(FILE)

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
	return datetime.isoformat(datetime.now())
