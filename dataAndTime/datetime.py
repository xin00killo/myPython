#coding:UTF-8
#__autor__='wyxces'

import time

# 当前时间错
ticks = time.time()
print('当前时间戳：', ticks)

structTime = time.struct_time
print(structTime.tm_year)

localtime1 = time.localtime(ticks)
print('当前时间为time.localtime(ticks)：', localtime1)
localtime2 = time.localtime()
print('当前时间为time.localtime()：', localtime2)



# 格式化成Sat Mar 28 22:24:24 2016形式
asctime = time.asctime(localtime2)
print('格式化的时间asctime：', asctime)

time1 = time.strftime("%a %b %d %H:%M:%S %Y", localtime1)
print('格式化的时间 %a %b %d %H:%M:%S %Y：', time1)
time1 = time.strftime("%A %B %d %H:%M:%S %Y", localtime1)
print('格式化的时间 %A %B %d %H:%M:%S %Y：', time1)


# 格式化成2016-03-20 11:45:39形式
time2 = time.strftime('%Y-%m-%d %H:%M:%S', localtime1)
print('格式化的时间%Y-%m-%d %H:%M:%S：', time2)

time2 = time.strftime('%Y-%m-%d %H:%M:%S %p', localtime1)
print('格式化的时间%Y-%m-%d %I:%M:%S %p ', time2)
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


time99 = time.strftime("%c", localtime1)
print('完整的格式化日期+时间 %c：', time99)
time99 = time.strftime("%j", localtime1)
print('年内的天 %j：', time99)

