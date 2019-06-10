#coding:UTF-8
#__autor__='wyxces'

import pymysql

#打开数据库连接
print('-------打开数据库连接-------------')
db = pymysql.connect('10.100.13.85', 'eagle', 'QAZmko%^&', 'test_db')
print('数据库连接成功',db)

#创建一个游标对象
print('-------创建一个游标对象-------------')
cursor = db.cursor()

cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print(data)

#删除表
print('-------删除表-------------')
sql = '''DROP TABLE IF EXISTS EMPLOYEE'''
cursor.execute(sql)

#新建表
print('-------新建表-------------')
sql = '''
    CREATE TABLE EMPLOYEE(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT)'''
cursor.execute(sql)

# 数据库插入操作
print('-------数据库插入操作-------------')
sql = '''
    INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX ,INCOME) 
        VALUES('WYX','CES',20,'M',100)
'''
cursor.execute(sql)
print('-------数据库插入操作-------------')
sql = '''
    INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX ,INCOME) 
        VALUES('%s','%s',%s,'%s',%s)
    '''%('WYX1','CE1S',210,'M',1010)
try:
    cursor.execute(sql)
except Exception as msg:
    db.rollback()
    print(msg)

print('-------数据库插入操作-------------')
sql = '''
    INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX ,INCOME) 
        VALUES(%s,%s,%s,%s,%s)
    '''
value = ('WYX2', 'CE2S', 20, 'S', 102)
try:
    cursor.execute(sql,value)
except Exception as msg:
    db.rollback()
    print(msg)
db.commit()


# 查询
print('------查询-------------')
sql = 'SELECT * FROM EMPLOYEE WHERE INCOME > %s' % (100)
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
        fname = result[0]
        iname = result[1]
        age = result[2]
        sex = result[3]
        income = result[4]
        print('result:', result)
        print('fname=%s,iname%s, age=%s,sex=%s,income=%s'
              % (fname, iname, age, sex, income))
except Exception as msg:
    print(msg)

#更新
print('------更新-------------')
sql = 'UPDATE EMPLOYEE SET AGE = AGE+1 WHERE SEX = "%c" ' % ('M')
try:
    cursor.execute(sql)
    db.commit()
except Exception as msg:
    db.rollback()
    print(msg)

# 删除
print('------删除-------------')
sql = 'DELETE FROM EMPLOYEE WHERE AGE > %s'%(20)
try:
    cursor.execute(sql)
    db.commit()
except Exception as msg:
    db.rollback()
    print(msg)



#关闭数据库连接
db.close()