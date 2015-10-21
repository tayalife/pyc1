# -*- coding: utf-8 -*-

# 输入输出和运行的软件和系统环境默认的encoding方式有关系
# Win7下面的情况
# Pycharm的IDE和Project encoding设置
# windows的默认GBK
# Pycharm: python-console interactive
# Pycharm: python filename.py
# PowerShell/Cmd: python-console interactive
# PowerShell/Cmd: python filename.py

# 输出
'欢迎光临'
u'欢迎光临'
'欢迎光临'.decode('utf-8')
u'欢迎光临'.encode('utf-8')

print '欢迎光临'
print u'欢迎光临'
print u'欢迎光临'.encode('utf-8')
print '欢迎光临'.decode('utf-8')


# 输入也要受到环境影响
tt = raw_input('input')
print type(tt)

if isinstance(tt, str):
    # Pycharm 设置了IDE和Project都为UTF8
    tt = tt.decode('utf-8')
    # 在windows的gbk环境下，解码
    # tt = tt.decode('gbk')

print type(tt)
print tt

