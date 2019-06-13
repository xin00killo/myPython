#coding:UTF-8
#__autor__='wyxces'

import pymongo

# 连接数据库
myclient = pymongo.MongoClient('10.100.19.63', 27017)
print('mongoDB连接成功：'.center(30,'-'), '\n', myclient)

#查询所有的库
dblist = myclient.list_database_names()
print('mongoDB 中库列表为：'.center(30,'-'))
for db in dblist:
    print(db)

# 进入mongoDB中的某个库
mydb = myclient['eagle']
print('mongoDB-eagle连接成功：'.center(30,'-'), '\n', mydb)

# 查询eagle下的集合信息
collist = mydb.list_collection_names()
print('eagle 中集合为：'.center(30,'-'))
for coll in collist:
    print(coll)

# 进入eagle中的某个集合
mycol = mydb['eagle_riskcon_third_log']
print('mongoDB-eagle-eagle_riskcon_third_log连接成功：'.center(50,'-'), '\n', mycol)


#使用 find_one() 方法来查询集合中的一条数据。
x = mycol.find_one()
print('集合中的一条数据:'.center(30,'-'), '\n', x)

#查询指定字段的数据
x = mycol.find_one({'ipId':1906121, 'themeCode':'RIM00119'})
print('1906121:'.center(30,'-'), '\n', x)

#查询集合中所有数据 find()
# for x in mycol.find():
#   print(x)

print('查询集合中所有数据 find()：print(result[id])'.center(50,'-'))
results = mycol.find({'ipId':1906121, 'themeCode':'RIM00119'})
for result in results:
    print(result['_id'])
print('-------------按_id倒序排序------------------------------------')
results = mycol.find({'ipId':1906121, 'themeCode':'RIM00119'}).sort('_id',pymongo.DESCENDING)
for result in results:
    print(result['_id'])
print('-------------按sendTime倒序排序并限定条数------------------------------------')
results = mycol.find({'ipId':1906121, 'themeCode':'RIM00119'}).sort('sendTime',pymongo.DESCENDING).limit(1)
for result in results:
    print(result)

