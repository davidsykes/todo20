#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import os
import traceback
from httpserverwrapper import HTTPServerWrapper
from requestobject import RequestObject

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			url = self.path
			self.logger.log('Get: %s from %s' % (url, self.client_address[0]))

			wrapper = HTTPServerWrapper(self)
			request = RequestObject.create_get_request(url, wrapper)
			self.url_handler.handle_request(url, request)


# 			# Return html, css or js files direction
# 			if ((len(self.path) > 5) and ((self.path[-5:] == '.html') or (self.path[-4:] == '.css') or (self.path[-3:] == '.js'))):
# 				f = open("."+self.path,"rb")
# 				self.send_response(200)
# 				if self.path[-4:] == '.css':
# 					self.send_header('Content-type', 'text/css')
# 				else:
# 					self.send_header('Content-type', 'text/html')
# 				self.end_headers()
# 				self.wfile.write(f.read())
# 				f.close()
# 				return

# #------------- *.png/ico/jpg -----------------------
# 			elif self.path.lower().endswith(".png") or self.path.lower().endswith(".ico") or self.path.lower().endswith(".jpg") or self.path.lower().endswith(".woff") or self.path.lower().endswith(".tff"):
# 				path = None
# 				if os.path.isfile("."+self.path):
# 					path = "."+self.path
# 				elif os.path.isfile("./Icons"+self.path):
# 					path = "./Icons"+self.path
# 				if path:
# 					f = open(path,"rb")
# 					self.send_response(200)
# 					if self.path.lower().endswith(".jpg"):
# 						self.send_header('Content-type', 'image/jpg')
# 					else:
# 						self.send_header('Content-type', 'image/png')
# 					self.end_headers()
# 					self.wfile.write(f.read())
# 					f.close()
# 				else:
# 					print ('404:', self.path)
# 					self.send_response(404)
# 					self.end_headers()
# 					self.wfile.write("Not Found: %s" % self.path)
# 				return

# #------------- Home or unrecognised -----------------------
# 			else:
# 				self.EndHeaders()
# 				message = None
# 				if self.path != '/Home' and self.path != '/' and self.path != '/m':
# 					print ('Unrecognised url', self.path)
# 					message = self.path
			return


#		except JukeboxException as e:
#			print 'JukeboxException "', str(e), '"', e.value
#			je = {}
#			je['exception'] = True
#			je['message'] = e.value
#			je['message'] = je['message'] + "\n\n" + traceback.format_exc(10)
#			self.send_response(505)
#			response = json.dumps(je)
#			self.end_headers()
#			self.wfile.write(response)

		except Exception as e:
			print ('UNEXPECTED GET EXCEPTION', e)
			print ('path', self.path)
			je = {}
			je['exception'] = True
			je['message'] = str(e)
			je['message'] = je['message'] + "\n" + traceback.format_exc(10)
			self.send_response(505)
			response = json.dumps(je)
			self.end_headers()
			self.wfile.write(response)
			raise

#		except IOError, e:
#			print 'Exception!'
#			print 'File Not Found: %s %s' % (self.path, str(e))
#			self.send_error(404,'File Not Found: %s %s' % (self.path, str(e)))
#		except SQLiteDatabaseError, e:
#			print 'Exception!'
#			print 'SQLiteDatabaseError', e, e.value

	def do_POST(self):
		print ('POST:', self.path)
		try:
			returnvalue = 'urg'
			self.send_response(200)
			print ('Send response 200')
			self.send_header('Content-type',	'text/json')
			self.end_headers()
			self.wfile.write(returnvalue)

		except Exception as e:
			print ('POST EXCEPTION', e)
			print ('path', self.path)
			je = {}
			je['exception'] = True
			je['message'] = str(e)
			je['message'] = je['message'] + "\n" + traceback.format_exc(10)
			self.send_response(505)
			response = json.dumps(je)
			self.end_headers()
			self.wfile.write(response)

	def EndHeaders(self):
		self.send_response(200)
		self.send_header('Content-type',	'text/html')
		self.end_headers()

	def send_code(self, response):
		self.send_response(response)

	def send_text_header(self):
		self.send_header('Content-type',	'text/html')
		self.end_headers()

	def write(self, data):
		self.wfile.write(data.encode())


class ToDoHTTPServer(threading.Thread):
	def __init__(self, factory, logger):
		self.factory = factory
		self.logger = logger
		threading.Thread.__init__(self, name='ToDo20')
		self.setDaemon(True)
		self.start()

	def run(self):
		self.logger.log('Try web server on port 8080')
		server = HTTPServer(('', 8080), MyHandler)
		self.logger.log('started httpserver...')
		MyHandler.logger = self.logger
		#MyHandler.wrapper = HTTPServerWrapper(server)
		MyHandler.url_handler = self.factory.fetch('UrlHandler')
		server.serve_forever()
