#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, time,queue
from multiprocessing.managers import BaseManager

#发送任务队列
task_queue = queue.Queue()

# 接收结果队列
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue', callable=lambda:task_queue)
QueueManager.register('get_result_queue', callable=lambda:result_queue)

# 绑定端口50000，设置验证码'abc'
manager = QueueManager(address=('',5000),authkey=b'abc')

manager.start()

# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()


for i in range(10):
	n = random.randint(0,10000)
	print('Put task %d ...'  % n)
	task.put(n)

print('Try get result ...')
for i in range(10):
	try:
		r = result.get(timeout=10)
		print('Result :%s' % r)
	except Queue.Empty:
		print('task queue is empty')
	finally:
		print('end')

manager.shutdown()
print('master exit')

