#/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import logging;logging.basicConfig(level=logging.INFO)

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
	lo