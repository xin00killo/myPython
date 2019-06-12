#coding:UTF-8
#__autor__='wyxces'

from datetime import *
print("datatime模块".center(50,"-"))

print('----------date-- 年 月  日 的操作---------------------------------')
print('----------date 静态方法和字段-----------------------------------')
print('(2019,6,12):', date(2019,6,12))
print('date.max:', date.max)
print('date.min:', date.min)
print('date.resolution:', date.resolution)
print('date.today()', date.today())
print('date.fromtimestamp(123456.89):', date.fromtimestamp(123456.89))

print('----------date 方法和属性-----------------------------------')
nowday = date.today()
print('day:%s:%s年%s月%s日'%(nowday, nowday.year, nowday.month, nowday.day))
# d1.replace(year, month, day)：生成一个新的日期对象，
# 用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
tomorrow = nowday.replace(day = nowday.day+1)
print('tomorrow：', tomorrow)
print('nowday.timetuple()：', nowday.timetuple())
print('nowday.weekday():', nowday.weekday())
print('nowday.isoweekday()', nowday.isoweekday())
print('2019,6,16是周几？  是周', date(2019,6,16).isoweekday())
print('nowday.isocalendar()', nowday.isocalendar())
print('tomorrow.isocalendar()', tomorrow.isocalendar())
print('nowday.isoformat():', nowday.isoformat())
print('%y,%m,%d,%H:', nowday.strftime('%y,%m,%d,%H'))



print('----------time--时 分 秒 毫秒 时区----------------------------------')
print('----------time 静态方法和字段-----------------------------------')
print('time(16,54,33,123456)：', time(16,54,33,123456))
print('time.max', time.max)
print('time.min', time.min)
print('time.resolution', time.resolution)

print('----------time 方法和属性-----------------------------------')
nowtime = time(16,54,33,123456)
print('nowtime = time(16,54,33):', nowtime)
print('nowtime.hour', nowtime.hour)
print('nowtime.minute', nowtime.minute)
print('nowtime.second', nowtime.second)
print('nowtime.microsecond', nowtime.microsecond)
print('nowtime.tzinfo', nowtime.tzinfo)
nexttime = nowtime.replace(hour=nowtime.hour+1)
print('nexttime ', nexttime)
print('nowtime.isoformat', nowtime.isoformat())
print('%H,%M,%S:', nowtime.strftime('%H,%M,%S'))



print('----------datetime--年 月 日 时 分 秒 毫秒 时区----------------------------------')
print('----------datetime 静态方法和字段-----------------------------------')
print('datetime.today():', datetime.today())
print('datetime.now():', datetime.now())
print('datetime.utcnow():', datetime.utcnow())
print('datetime.fromtimestamp(123456.789)：', datetime.fromtimestamp(123456.789))
print('datetime.utcfromtimestamp(123456.789)', datetime.utcfromtimestamp(123456.789))
print('datetime.combine(nowday,nowtime):', datetime.combine(nowday,nowtime))
datetime_str =  nowday.strftime('%Y,%m,%d,%H') + ',' + nowtime.strftime('%H,%M,%S')
# print(datetime_str)
# print("datetime.strptime(datetimeobj, '%Y,%m,%d %H,%M,%S')", datetime.strptime(datetime_str, '%Y,%m,%d,%H,%M,%S'))

print('----------datetime 方法和属性-----------------------------------')
datetimeobj = datetime.today()
print('datetimeobj = datetime.today()', datetimeobj)
print('datetimeobj.today():', datetimeobj.today())
print('datetimeobj.year():', datetimeobj.year)
print('datetimeobj.month():', datetimeobj.month)
print('datetimeobj.day():', datetimeobj.day)
print('datetimeobj.hour():', datetimeobj.hour)
print('datetimeobj.minute():', datetimeobj.minute)
print('datetimeobj.second():', datetimeobj.second)
print('datetimeobj.microsecond():', datetimeobj.microsecond)
print('datetimeobj.date():', datetimeobj.date())
print('datetimeobj.time():', datetimeobj.time())
print('datetimeobj.timetuple():', datetimeobj.timetuple())
print('datetimeobj.utctimetuple():', datetimeobj.utctimetuple())
print('datetimeobj.toordinal():', datetimeobj.toordinal())
print('datetimeobj.weekday():', datetimeobj.weekday())
print('datetimeobj.isoweekday():', datetimeobj.isoweekday())
print('datetimeobj.isocalendar():', datetimeobj.isocalendar())
print('datetimeobj.ctime():', datetimeobj.ctime())
print('datetimeobj.ctime():', datetimeobj.ctime())



print('----------timedelta--时间加减----------------------------------')
dt = datetime.now()
print('dt = datetime.now():', dt)
print('dt + timedelta(days=-1):', dt + timedelta(days=-1))
print('dt - timedelta(days=1):', dt - timedelta(days=1))
print('dt + timedelta(days=1):', dt + timedelta(days=1))
print('timedelta(days=1):', timedelta(days=1))
print('timedelta(days=-1):', timedelta(days=-1))
print('timedelta(days=1).days():', timedelta(days=1).days)
print('timedelta(days=1).total_seconds():', timedelta(days=1).total_seconds())
print('timedelta(days=1,seconds=60):', timedelta(days=1,seconds=60))

print('----------tzinfo--时区----------------------------------')
#from datetime import datetime, tzinfo,timedelta
class UTC(tzinfo):
    def __init__(self,offset = 0):
        self._offset = offset
    def utcoffset(self, dt):  #标准时间的位移
        return timedelta(hours=self._offset)
    def tzname(self, dt):
        return "UTC +%s" % self._offset
    def dst(self, dt): #Daylight Saving Time的缩写,夏时制
        return timedelta(hours=self._offset)
beijing = datetime(2011,11,11,0,0,0,tzinfo = UTC(8))
print(beijing)
print(UTC(8))