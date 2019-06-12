#coding=utf-8
# __autor__='wyxces'

import calendar

cal = calendar.month(2019,6)
print('输出2019.06的日历\n',cal)




'''calendar.calendar(year,w=2,l=1,c=6,m=3)
返回多行字符串格式的year年年历
w 月日历内 横向距离
c 月日历间横向距离
I 竖向距离
m 每排显示月数
'''
cal = calendar.calendar(2019,w=2,l=1,c=6,m=4)
print('输出2019的日历\n',cal)


'''calendar.firstweekday( )
返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
'''
print('当前每周起始日期的设置:', calendar.firstweekday( ))


'''calendar.isleap(year)
是闰年返回 True，否则为 false。
'''
print('今年2019是否为闰年：', calendar.isleap(2019))


'''calendar.leapdays(y1,y2)
返回在Y1，Y2两年之间的闰年总数。
'''
print('1989`2019之间，闰年总数为：', calendar.leapdays(1989, 2019))


'''calendar.month(year,month,w=2,l=1)
返回一个多行字符串格式的year年month月日历，两行标题，一周一行。
每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
'''
print(calendar.month(2019,9,0,0))
print(calendar.month(2019,9,10,2))


'''calendar.monthcalendar(year,month)
返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。
Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
'''
print('2019,6:', calendar.monthcalendar(2019,6))
print('2019,5:', calendar.monthcalendar(2019,5))


'''calendar.monthrange(year,month)
返回两个整数。第一个是该月的星期几，第二个是该月有几天。星期几是从0（星期一）到 6（星期日）。
'''
print('(2019,6)的第一天是周几和天数：', calendar.monthrange(2019,6))
print(type(calendar.monthrange(2019,6)))


'''	calendar.prcal(year,w=2,l=1,c=6)
相当于 print calendar.calendar(year,w,l,c).
'''
# calendar.prcal(2019)


'''	calendar.prmonth(year,month,w=2,l=1)
相当于 print calendar.calendar（year，w，l，c）。
'''
# calendar.prmonth(2019, 6)


'''calendar.timegm(tupletime)
和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）。
'''
import time
t = (2016, 2, 17, 17, 3, 38, 1, 48, 0)
ticks = calendar.timegm(t)
print('calendar.timegm((2016, 2, 17, 17, 3, 38, 1, 48, 0)): ', ticks)


'''calendar.weekday(year,month,day)
返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
'''
weekday = calendar.weekday(2019, 6, 12)
print('20190612的日期码为：%s, 即 周 %s' %(weekday, weekday+1))


'''	calendar.setfirstweekday(weekday)
设置每周的起始日期码。0（星期一）到6（星期日）。
'''
calendar.setfirstweekday(0)
print('设置每周的其实日期码为0时：')
calendar.prmonth(2019, 6)
print()
calendar.setfirstweekday(6)
print('设置每周的其实日期码为6时：')
calendar.prmonth(2019, 6)
