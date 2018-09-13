#/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import logging;logging.basicConfig(level=logging.INFO)
import aiomysql

# async def hello():
# 	print('hello world!')
# 	r = await asyncio.sleep(1)
# 	print('hello again!')

# from aiohttp import web

# async def index(request):
# 	await asyncio.sleep(0.5)
# 	return web.Response(body='<h1>Index</h1>'.encode() ,content_type='text/html')

# async def hello(request):
# 	await asyncio.sleep(0.5)
# 	text = '<h1>hello %s!</h1>' % request.match_info['name']
# 	return web.Response(body=text.encode('utf-8'),content_type='text/html')

# async def init(loop):
# 	app = web.Application(loop=loop)
# 	app.router.add_route('GET', '/' ,index)
# 	app.router.add_route('GET', '/hello/{name}' ,hello)
# 	srv = await loop.create_server(app.make_handler(), '127.0.0.1' ,8000)
# 	print('Server started at http://127.0.0.0.1:8000...')
# 	return srv

# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()

async def create_pool(loop, **kw):
	logging.info('create database connection pool...')
	global __pool
	__pool = await aiomysql.create_pool(
		host=kw.get('host','localhost'),
		port=kw.get('port',3306),
		user=kw['user'],
		password=kw['password'],
		db=kw['db'],
		charset=kw.get('charset','utf8'),
		autocommit=kw.get('autocommit',True),
		maxsize=kw.get('maxsize',10),
		minsize=kw.get('minsize',1),
		loop=loop)

async def select(sql, args, size=None):
	log(sql,args)
	global __pool
	with yield from __pool as conn:
		cur = await conn.cursor(aiomysql.DictCursor)
		await from cur.execute(sql.replace('?','%s'), args, or ())
		if size:
			rs = await cur.fetchmany(size)
		else:
			rs = await cur.fetchall()
		await cur.close()
		logging.info('rows return:%s' % len(rs))
		return rs

async def execute(sql, args):
	log(sql)
	with await __pool as conn:
		try:
			cur = await conn.cursor()
			await cur.execute(sql.replace('?','%s'),args)
			affected = cur.rowcount()
			await cur.close()
		except BaseException as e:
			raise 
		return affected

