#coding:UTF-8
#__autor__='wyxces'


'''
33、log日志中，我们需要用时间戳记录error,warning等的发生时间，
请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
'''
import logging
from datetime import datetime

msg = 'wyxces msg'
print(datetime.now(),' ',msg)
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),' ',msg)

# logging.error(msg , datetime.now())

