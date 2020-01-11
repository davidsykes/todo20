#!/usr/bin/env python

import time
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
from urlhandler import UrlHandler
from urldissector import UrlDissector
from urlrouter import UrlRouter
from defaultdestination import DefaultDestination

sys.path.append('../pagegroups/testpagegroup/src')
from pagegroup import TestPageGroup

rvPermanentError = 9
DAILY_LOG_NAME = 'todolog'
DAILY_LOG_EXT = 'log'


try:
	factory = Factory()
	factory.register('DateTimeWrapper', DateTimeWrapper())
	factory.register('FsWrapper', FsWrapper())
	logger = LogChainer(DailyFileLogger(factory, DAILY_LOG_NAME, DAILY_LOG_EXT))
	logger.chain(ConsoleLogger(True))
	factory.register('Logger', logger)
	factory.register('UrlDissector', UrlDissector())
	factory.register('UrlRouter', UrlRouter(DefaultDestination()))
	factory.register('UrlHandler', UrlHandler(factory))

	factory.fetch('UrlRouter').register_destination('test', TestPageGroup())

	httpserver = ToDoHTTPServer(factory, logger)

	while True:
		time.sleep(1)
except KeyboardInterrupt:
	if logger != None:
		logger.log('Ctrl C received')
	sys.exit(rvPermanentError)
