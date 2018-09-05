#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
re.match(r'^\d{3}\-\d{3,8}&','010-123456')


m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

import re

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-123456').groups())
print(re_telephone.match('010-8086').groups())


from datetime import datetime
dt = datetime(2015, 4, 19, 12, 20)
print(dt.timestamp())
t = 1429417200
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))



def is_valid_email(addr):
	reg = r'[a-zA-Z0-9\.]+@\w+\.com'
	if(re.match(reg,addr)):
		return True
	else:
		return False

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


import base64
def safe_base64_decode(s):
	if len(s) % 4 != 0:
		num = 4 - len(s) % 4
		s = s + b'=' * num
	return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

enStr = base64.b64encode(b'binary\x00string')
print(enStr)
deStr = base64.b64decode(enStr)
print(deStr)

import itertools
def pi(N):
	natuals = itertools.count(1, 2)
	ns = itertools.takewhile(lambda x:x <= 2*N - 1, natuals)
	ns = map(lambda x:(-1)**(x//2) * 4/x,ns)
	return sum(ns)


print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')


class Query(object):

	def __init__(self, name):
		self.name = name

	def __enter__(self):
		print('Begin')
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		if exc_type:
			print('Error')
		else:
			print('End')

	def query(self):
		print('Query info about %s ...' % self.name)

with Query('Bob') as q:
	q.query()


from contextlib import contextmanager
class Query(object):
	def __init__(self, name):
		self.name = name
	def query(self):
		print('Query info about %s ...' % self.name)


@contextmanager
def create_query(name):
	print('Begin')
	q = Query(name)
	yield q
	print('End')

with create_query('Bob') as q:
	q.query()
	

@contextmanager
def tag(name):
	print('<%s>' % name)
	yield
	print('</%s>' % name)

with tag('h1'):
	print('hello')
	print('world')


from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
	for line in page:
		print(line)


@contextmanager
def closing(thing):
	try:
		yield thing
	finally:
		thing.close()


from urllib import request
import json


def fetch_data(url):
	req = request.Request(url)
	with request.urlopen(req) as f:
		print('Status:', f.status, f.reason)
		for k,v in f.getheaders():
			print('%s:%s' % (k, v))
		data = f.read()
		data = json.loads(data)
		return data


URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')


from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):

	def start_element(self, name, attrs):
		print('sax:start_element: %s, attrs %s' % (name, str(attrs)))

	def end_element(self, name):
		print('sax:end_element: %s ' % name)

	def char_data(self, text):
		print('sax:char_data:%s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parsers = ParserCreate()
parsers.StartElementHandler = handler.start_element
parsers.EndElementHandler = handler.end_element
parsers.CharacterDataHandler = handler.char_data
parsers.Parse(xml)



