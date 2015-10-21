# -*- coding: utf-8 -*-
import requests
# 'http://www.zhidaow.com/post/python-requests-install-and-brief-introduction'

r = requests.get('http://newsmth.net/frames.html')
r = requests.get('http://www.newsmth.net/nForum/#!article/Python/84709?p=3')
print r.status_code
print r.headers['content-type']
print r.encoding
tt = r.text
print tt.encode('utf-8')
print tt.encode('ISO-8859-1')