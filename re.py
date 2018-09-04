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
	