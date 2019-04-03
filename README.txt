Author:
	Tanner.L.Woody@gmail.com
Date:
	2019-03-29

Purpose:
	Keep all familiar and regurally used scripts in one place.

Dependencies:
	NA

Resources:
	Self:
		$HOME/Library/Python/3.7/lib/python/site-packages/pytils
	Loggins:
		~/.pylog/
	Archiving:
		~/.attic/

Tests:
	clear && python3 tests/Tests.py
	All information stored in ~/.pylog/logs/main.log
	For Verbosity:
		FLAGS['isVerbose'] = True
		Set in /pytils/config.py or any desired test case.
		TODO: Add an argument to make verbose from cmd line;
