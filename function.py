# -*- coding: utf-8 -*-
def power(x):
	return x * x

print(power(5))
print(power(15))

def power(x,n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

print(power(5,2))
print(power(5,3))
#power(5)
def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
power(3)

def product(*arg):
	sum = 0
	if len(arg) is 0:
		sum = 0
	for va in arg:
		sum = sum * va
	return sum
print(product())
print(product(1,2,3,5,7))

def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)
print(fact(1))
print(fact(5))
print(fact(100))

def move(n,a,b,c):
	if n == 1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)

move(2,'A','B','C')

def trim(s):
	if s[:1] != ' ' and s[-1:] != ' ':
		return s
	elif s[:1] == ' ':
		s = s[1:]
		return trim(s)
	elif s[-1:] == ' ':
		s = s[:-1]
		return trim(s)

print(trim('  ffefefe   '))

from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

for i, value in enumerate(['a','b','c']):
	print(i,value)

import math
def findMinAndMax(l):
	if len(l) == 0:
		return (None,None)
	max = l[0]
	min = l[0]
	for val in l:
		if val >= max:
			max = val
		if val <= min:
			min = val
	return (min,max)
		

if findMinAndMax([]) != (None, None):
    print('测试失败!1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!4')
else:
    print('测试成功!')

x = [x.lower() for x in ['Hello', 'World', 18, 'Apple', None] if isinstance(x,str)]
print(x)

import time

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def now():
	print('2015-3-25')
now()

def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
	
@log('excute')
def now():
	print('2015-3-25')
now()

import time
import functools

def metric(func):
	@functools.wraps(func)
	def wrapper(*arg,**kw):
		pre = time.time()
		re = func(*arg,**kw)
		after = time.time()
		print('%s excuted in %s ms' % (func.__name__, time.time()))
		return re
	return wrapper
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!',fast.__name__)
# elif s != 7986:
#     print('测试失败!',slow.__name__)


def logDecorator(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		return func(*args, **kw)
	return wrapper
	

def logText(*s):
 	def decorator(func):
 		@functools.wraps(func)
 		def wrapper(*args,**kw):
 			print('begin call:')
 			re = func(*args,**kw)
 			print('end call :')
 			return re
 		return wrapper
 	return decorator

# @logText
# def f():
#  	return 1
# f()

@logText('execute')
def f():
 	return 2
f()

def partial(func, *part_args):
	def wrapper(*extra_args):
		return func(*part_args+extra_args)
	return wrapper

def my_partial(func, *args, **kw):
	@functools.wraps(func)
	def wrapper(*arg):
		return func(*args+arg, **kw)
	return wrapper

def add(x, y, z):
	return x + y + z

addd = partial(add,2,3)
print(addd(4),addd.__name__)


class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s: %s' % (self.name,self.score))


class Screen(object):
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self,value):
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self,value):
			self._height = value

	@property
	def resolution(self):
		return self._width * self._height
		

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a, self.b = 0,1

	def __iter__(self):
		return self

	def __next__(self):
		self.a,self.b = self.b,self.a + self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a


class Chain(object):
	"""docstring for Chain"""
	def __init__(self, path = ''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path,path))

	def __call__(self,path = ''):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	#__repr__ == __str__

test = Chain().status.user.timeline.list
print(test)

test2 = Chain().user('snow').repos
print(test2)
		
		
from enum import Enum, unique

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)



@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Web = 3
	Thu = 4
	Fri = 5
	Sat = 6

day1 = Weekday.Mon
print(day1)

class Gender(Enum):
	Male = 0
	Female = 1

class Student(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
	print('pass')
else:
	print('failed')


def fn(self,name = 'world'):
	print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()


class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)


class MyList(list,metaclass=ListMetaclass):
	pass
		
L = MyList()
L.add(1)
print(L)
	
		


