#!/usr/bin/env python

import sys
import os
import sqlite3
sys.path.append('../../temperatures/Library/src')

from factory import Factory
from fs_wrapper import FsWrapper
from parameters import Parameters, ParamError
from sqlite_database import SQLiteDatabase, SQLiteDatabaseError

def Usage(mess):
	print(mess)
	print('Usage: ' + sys.argv[0] + " -db {Path to the db} -q {select query} -Q {path to query file} -x {execute query}")
	sys.exit(0)

def run_script(database, script_file):
	with open(script_file) as source_file:
		sql_script = source_file.read()
		return database.executescript(sql_script)

def output_query_result(res):
	if res == None:
		print('None')
	else:
		for r in res:
			print(r)
		print('---')

factory = Factory()
factory.register('FsWrapper', FsWrapper())

try:
	p = Parameters(factory, ['?'],['db','q', 'Q', 'x', 'f'],[], sys.argv[1:])
except ParamError as e:
	Usage('Param error: ' + e.value )

if p.get_switch('?'):
	print('select * from Collections')
	print("update Collections set name='Davids' where name = 'pop'")
	sys.exit(0)

if p.get_option('db') == None:
	Usage('db missing')
if not os.path.isfile(p.get_option('db')):
	Usage('db not found')

try:
	database = SQLiteDatabase(sqlite3.connect(p.get_option('db'), check_same_thread = False))

	if p.get_option('q') != None:
		res = database.query(p.get_option('q'))
		output_query_result(res)
	elif p.get_option('Q') != None:
		with open(p.get_option('Q')) as source_file:
			sql_script = source_file.read()
			res = database.query(sql_script)
			output_query_result(res)
	elif p.get_option('x') != None:
		res = database.execute_with_commit(p.get_option('x'))
		print(res)
	elif p.get_option('f') != None:
		res = run_script(database, p.get_option('f'))
		print(res)
	else:
		print('Missing query')

except SQLiteDatabaseError as e:
	print('Got an exception SQLiteDatabaseError: ', str(e))
