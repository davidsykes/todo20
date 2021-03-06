#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import os
import traceback
from httpserverwrapper import HTTPServerWrapper
from requestobject import RequestObject
from todoexception import ToDoException

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			url = self.path
			self.logger.log('Get: %s from %s' % (url, self.client_address[0]))

			wrapper = HTTPServerWrapper(self)
			request = RequestObject.create_get_request(url, wrapper)
			self.url_request_handler.handle_request(url, request)
			return

		except ToDoException as e:
			self.logger.log('ToDoException: %s' % (str(e)))
			self.logger.error('ToDoException: %s' % (str(e)))
			self.logger.log('Stack: %s' % (traceback.format_exc(10)))

			self.send_response(500)
			response = 'exception'
			self.end_headers()
			self.write_text(response)
			return

		except Exception as e:
			self.logger.error('Exception: %s' % (str(e)))
			self.logger.error('Path: %s' % (self.path))
			self.logger.error('Stack: %s' % (traceback.format_exc(10)))

			self.send_response(500)
			response = 'exception'
			self.end_headers()
			self.write_text(response)
			return

	def do_POST(self):
		try:
			url = self.path
			self.logger.log('Post: %s from %s' % (url, self.client_address[0]))

			wrapper = HTTPServerWrapper(self)
			request = RequestObject.create_post_request(url, wrapper)
			self.url_request_handler.handle_request(url, request)
			return

		except ToDoException as e:
			self.logger.log('ToDoException: %s' % (str(e)))
			self.logger.error('ToDoException: %s' % (str(e)))
			self.logger.log('Stack: %s' % (traceback.format_exc(10)))

			self.send_response(500)
			response = 'exception'
			self.end_headers()
			self.write_text(response)
			return

		except Exception as e:
			self.logger.error('Exception: %s' % (str(e)))
			self.logger.error('Path: %s' % (self.path))
			self.logger.error('Stack: %s' % (traceback.format_exc(10)))

			self.send_response(500)
			response = 'exception'
			self.end_headers()
			self.write_text(response)
			return


	# region wrapper

	def send_code(self, response):
		self.send_response(response)

	def send_header(self, content, type):
		super().send_header(content, type)

	def end_headers(self):
		super().end_headers()

	def write_text(self, data):
		self.wfile.write(data.encode())

	# end region



	def EndHeaders(self):
		self.send_response(200)
		self.send_header('Content-type',	'text/html')
		self.end_headers()



class ToDoHTTPServer(threading.Thread):
	def __init__(self, factory):
		self.factory = factory
		self.logger = factory.fetch('Logger')
		threading.Thread.__init__(self, name='ToDo20')
		self.setDaemon(True)
		self.start()

	def run(self):
		self.logger.log('Try web server on port 8080')
		server = HTTPServer(('', 8080), MyHandler)
		self.logger.log('started httpserver...')
		MyHandler.factory = self.factory
		MyHandler.logger = self.logger
		MyHandler.url_request_handler = self.factory.fetch('UrlRequestHandler')
		server.serve_forever()
