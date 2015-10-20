# -*- coding: utf-8 -*-
print 'hello py'
# tt = raw_input('input')

#python console(ascii)
print '欢迎光临'
print u'欢迎光临'.encode('utf-8')

# cmd python file.py (gbk)
print '欢迎光临'.decode('utf-8')
print u'欢迎光临'


tt = raw_input('input')
print type(tt)
if isinstance(tt, unicode):
    #python console
    print 'unicode:'
    print tt.encode('utf-8')
if isinstance(tt, str):
    #cmd
    print 'str:'
    print tt
