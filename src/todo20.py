#!/usr/bin/env python

#import os
#import sys
import time
#import sqlite3
#import threading
#import traceback
import sys
sys.path.append('../Library/src')
sys.path.append('../../temperatures/Library/src')
from fs_wrapper import FsWrapper
from datetime_wrapper import DateTimeWrapper
from logchainer import LogChainer
from console_logger import ConsoleLogger
from daily_file_logger import DailyFileLogger
from todohttpserver import ToDoHTTPServer
from factory import Factory

rvPermanentError = 9
DAILY_LOG_NAME = 'todolog'
DAILY_LOG_EXT = 'log'
#WEB_PATH = '/home/dev/Documents/temperatures/WebServer/www'


try:
	factory = Factory()
	factory.register('DateTimeWrapper', DateTimeWrapper())
	factory.register('FsWrapper', FsWrapper())
	logger = LogChainer(DailyFileLogger(factory, DAILY_LOG_NAME, DAILY_LOG_EXT))
	logger.chain(ConsoleLogger(True))
	factory.register('Logger', logger)

	httpserver = ToDoHTTPServer(factory, logger)

	while True:
		time.sleep(1)
except KeyboardInterrupt:
	if logger != None:
		logger.log('Ctrl C received')
	sys.exit(rvPermanentError)
