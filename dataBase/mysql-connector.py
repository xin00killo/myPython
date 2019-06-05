#coding:UTF-8
#__autor__='wyxces'

#Python MySQL - mysql-connector 驱动  菜鸟教程

import mysql.connector


# 创建数据库连接
mysqlDB = mysql.connector.connect(
    host = '99999',
    user = '99',
    passwd = '99%^&'
)
print('数据库连接：',mysqlDB)

mycursor = mysqlDB.cursor()  #  cursor (计算机荧光屏上的) 光标，游标;

# 创建数据库
mycursor.execute("CREATE DATABASE test_db")

# SHOW DATABASES  来查看数据库中所有的库
mycursor.execute('SHOW DATABASES')
print(mycursor)
for database in mycursor:
    print(database)

#直接连接数据库中的 某个库
testDB = mysql.connector.connect(
    host = '99999',
    user = '99',
    passwd = '99%^&',
    database = 'test_db'
)
print('test_db数据库连接：',testDB)

testcursor = testDB.cursor(buffered=True)   #  cursor (计算机荧光屏上的) 光标，游标;

# SHOW DATABASES  来查看数据库中所有的库
print('---------SHOW DATABASES  来查看数据库中所有的库--------------')
testcursor.execute('SHOW DATABASES')
print(testcursor)
for database in testcursor:
    print(database)

# 删除和创建数据表
print('---------删除和创建数据表--------------')
sql = 'DROP TABLE IF EXISTS test_table'
testcursor.execute(sql)
sql = 'CREATE TABLE test_table(name VARCHAR(255), url VARCHAR(255))'
testcursor.execute(sql)

#查看数据库表
print('---------查看数据库表--------------')
testcursor.execute('SHOW TABLES')
print(testcursor)
for table in testcursor:
    print(table)

# 主键设置
print('---------主键设置--------------')
sql='AlTER TABLE test_table ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'
testcursor.execute(sql)

#插入数据
print('---------插入数据--------------')
sql = 'INSERT INTO test_table (name,url) VALUES (%s,%s)'
val = ('WYX','www.wyx.com')
testcursor.execute(sql, val)
testDB.commit()

#批量插入
sql = 'INSERT INTO test_table (name,url) VALUES (%s,%s)'
val = [
    ('WYX1','www.wyx1.com'),
    ('WYX2','www.wyx2.com'),
    ('WYX3','www.wyx3.com')
]
testcursor.executemany(sql, val)
testDB.commit()
print('更新成功，共插入行数：%s行'%testcursor.rowcount)
print('最后一条插入的数据的id为：', testcursor.lastrowid)


#查询数据
print('---------查询数据--------------')
sql = 'SELECT * FROM test_table'
testcursor.execute(sql)
result = testcursor.fetchall()
print(sql, ':', result)
print('---------只查询一条数据--------------')
testcursor.execute(sql)
result = testcursor.fetchone()
print(sql, ':', result)
# results = testcursor.fetchall()
print('---------条件查询--------------')
sql = 'SELECT * FROM test_table WHERE  name LIKE %s'
val = ('WYX_',)
testcursor.execute(sql, val)
results = testcursor.fetchall()
print(sql, ':', results)
print('---------设定起始位置，限定查询数量--------------')
sql = 'SELECT * FROM test_table LIMIT 2 OFFSET 1'
testcursor.execute(sql)
results = testcursor.fetchall()
print(sql, ':',results)

#删除记录
print('---------删除记录-------------')
sql = 'DELETE FROM test_table WHERE  name = %s'
val = ('WYX2',)
testcursor.execute(sql,val)
testDB.commit()
print('---------gengxin记录-------------')
sql = 'UPDATE test_table SET name = %s WHERE id = %s'
val = ('wyxcesname', '4')
testcursor.execute(sql, val)
testDB.commit()

#关闭数据库连接
testDB.close()
mysqlDB.close()
