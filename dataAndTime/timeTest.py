#coding=utf-8
#__autor__='wyxces'

import time
print('--------时间戳/时间元组----------------------------------')
# 当前时间戳
ticks = time.time()
print('当前时间戳：', ticks)

print('系统运行时间:',time.perf_counter())  # 返回系统运行时间
print('进程运行时间:',time.process_time())  # 返回进程运行时间

# 时间元组
structTime = time.struct_time
print('时间元组：', structTime)
print('structTime.tm_year:', structTime.tm_year)

# 接收时间戳  并返回当地时间下的时间元组
ticks = 123456789.15
localtime1 = time.localtime(ticks)
print('ticks = 123456789.15,对应时间元组：', localtime1)
localtime = time.localtime()
print('当前时间为：', localtime)

# 接受时间元组，返回时间戳
t = (2016, 2, 17, 17, 3, 38, 1, 48, 0)
print('\n时间元组：', t)
secs = time.mktime( t )
print ("对应时间戳 : ", secs)
print ("时间为: %s" % time.asctime(time.localtime(secs)))


print('--------格式化----------------------------------')
# asctime  格式化成Sat Mar 28 22:24:24 2016形式
print('格式化的时间asctime：', time.asctime(localtime))
print ("格式化的时间time.ctime() :" , time.ctime())
# strftime 格式化时间
print('格式化的时间 %a %b %d %H:%M:%S %Y：', time.strftime("%a %b %d %H:%M:%S %Y", localtime))
print('格式化的时间 %A %B %d %H:%M:%S %Y：', time.strftime("%A %B %d %H:%M:%S %Y", localtime))


# 格式化成2016-03-20 11:45:39形式
print('格式化的时间%Y-%m-%d %H:%M:%S：', time.strftime('%Y-%m-%d %H:%M:%S', localtime))
print('格式化的时间%y-%m-%d %H:%M:%S：', time.strftime('%y-%m-%d %H:%M:%S', localtime))

# p  A.M  P.M
print('格式化的时间A.M /P.M %p :', time.strftime('%Y-%m-%d %H:%M:%S %p', localtime))

print('完整的格式化日期+时间 %c：', time.strftime("%c", localtime))
print('年内的天 %j：', time.strftime("%j", localtime))
print('一年中的星期数（周日为星期的开始） %U：', time.strftime("%U", localtime))
print('星期周日为星期的开始 0-6 %w：', time.strftime("%w", localtime))
print('一年中的星期数（周一为星期的开始） %W：', time.strftime("%W", localtime))

print('日期 %x：', time.strftime("%x", localtime))
print('时间 %X：', time.strftime("%X", localtime))
print('时区 %z：', time.strftime("%z", localtime))
print('时区 %Z：', time.strftime("%Z", localtime))


print('--------functions----------------------------------')
# sleep
print('当前时间为：', time.asctime(time.localtime()))
print('time.sleep(10)')
time.sleep(10)
print('当前时间为：', time.asctime(time.localtime()))

