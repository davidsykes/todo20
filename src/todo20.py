#!/usr/bin/env python

import time
import sys
sys.path.append('../Library/src')
sys.path.append('../../temperatures/Library/src')
from fs_wrapper import FsWrapper
from datetime_wrapper import DateTimeWrapper
from logchainer import LogChainer
from console_logger import ConsoleLogger
from dailyfilewriter import DailyFileWriter
from logger import Logger
from todohttpserver import ToDoHTTPServer
from factory import Factory
from urlrequesthandler import UrlRequestHandler
from urlvalidator import UrlValidator
from urlpagegroupextractor import UrlPagegroupExtractor
from urlrouter import UrlRouter
from defaultdestination import DefaultDestination
from dailyfilewriter import DailyFileWriter

sys.path.append('../pagegroups/testpagegroup/src')
from pagegroup import TestPagegroup
sys.path.append('../pagegroups/ttt/src')
from tttpagegroup import TickTackToePagegroup
sys.path.append('../pagegroups/todo/src')
from todopagegroup import ToDoPagegroup

rvPermanentError = 9
DAILY_LOG_NAME = 'applicationlog'
DAILY_LOG_EXT = 'log'
DAILY_ERR_EXT = 'err'


try:
	factory = Factory()
	factory.register('DateTimeWrapper', DateTimeWrapper())
	factory.register('FsWrapper', FsWrapper())

	daily_log_writer = DailyFileWriter(factory, DAILY_LOG_NAME, DAILY_LOG_EXT)
	daily_err_writer = DailyFileWriter(factory, DAILY_LOG_NAME, DAILY_ERR_EXT)
	daily_logger = Logger(factory, daily_log_writer, daily_err_writer)

	logger = LogChainer(daily_logger)
	logger.chain(ConsoleLogger(True))
	factory.register('Logger', logger)

	factory.register('UrlValidator', UrlValidator())
	factory.register('UrlPagegroupExtractor', UrlPagegroupExtractor())
	factory.register('UrlRouter', UrlRouter(DefaultDestination(factory, '/home/dev/Documents/todo20/www')))
	factory.register('UrlRequestHandler', UrlRequestHandler(factory))

	factory.fetch('UrlRouter').register_destination('test', TestPagegroup('/home/dev/Documents/todo20/pagegroups/testpagegroup/pages'))
	factory.fetch('UrlRouter').register_destination('ttt', TickTackToePagegroup('/home/dev/Documents/react/my-app/build'))
	factory.fetch('UrlRouter').register_destination('todo', ToDoPagegroup('/home/dev/Documents/react/my-app/build'))

	httpserver = ToDoHTTPServer(factory, logger)

	while True:
		time.sleep(1)
except KeyboardInterrupt:
	if logger != None:
		logger.log('Ctrl C received')
	sys.exit(rvPermanentError)
