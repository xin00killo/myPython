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
# for result in results:
#     print(result['_id'])
for result in results:
    print(result['sendTime'])
print('-------------按sendTime倒序排序并限定条数------------------------------------')
results = mycol.find({'ipId':1906121, 'themeCode':'RIM00119'}).sort('sendTime',pymongo.DESCENDING).limit(1)
for result in results:
    print(result)

#指定字段
print('-------------指定字段_id=0------------------------------------')
results = mycol.find({'ipId':1906121, 'themeCode':'RIM00119'},{'_id':0}).limit(1)
for result in results:
    print(result)
print('-------------指定字段_id=1------------------------------------')
results = mycol.find({'ipId':1906121, 'themeCode':'RIM00119'},{'_id':1}).limit(1)
for result in results:
    print(result)
print('-------------指定字段piecesNoId=1,ipId=1------------------------------------')
results = mycol.find({'ipId':1906121, 'themeCode':'RIM00119'},{'piecesNoId':1,'ipId':1,'sendTime':1}).limit(1)
for result in results:
    print(result)

#高级查询

print('-------------高级查询，sendTime < 1560412141------------------------------------')
myquery = {'ipId':1906121, 'themeCode':'RIM00119','sendTime':{'$lt':1560412141}}
mydoc = mycol.find(myquery)
for doc in mydoc:
    print(doc['_id'],doc['sendTime'])
print('-------------高级查询，sendTime > 1560412141------------------------------------')
myquery = {'ipId':1906121, 'themeCode':'RIM00119','sendTime':{'$gt':1560412141}}
mydoc = mycol.find(myquery)
for doc in mydoc:
    print(doc['_id'],doc['sendTime'])
print('-------------高级查询，sendTime <= 1560412141------------------------------------')
myquery = {'ipId':1906121, 'themeCode':'RIM00119','sendTime':{'$lte':1560412141}}
mydoc = mycol.find(myquery)
for doc in mydoc:
    print(doc['_id'],doc['sendTime'])
print('-------------高级查询，sendTime >= 1560412141------------------------------------')
myquery = {'ipId':1906121, 'themeCode':'RIM00119','sendTime':{'$gte':1560412141}}
mydoc = mycol.find(myquery)
for doc in mydoc:
    print(doc['_id'],doc['sendTime'])
print('-------------高级查询，sendTime <> 1560412141------------------------------------')
myquery = {'ipId':1906121, 'themeCode':'RIM00119','sendTime':{'$ne':1560412141}}
mydoc = mycol.find(myquery)
for doc in mydoc:
    print(doc['_id'],doc['sendTime'])
print('-------------高级查询，sendTime in  [1560412320,1560501996]------------------------------------')
myquery = {'ipId':1906121, 'themeCode':'RIM00119','sendTime':{'$in':[1560412320,1560501996]}}
mydoc = mycol.find(myquery)
for doc in mydoc:
    print(doc['_id'],doc['sendTime'])
print('-------------高级查询，sendTime nin  [1560412320,1560501996]------------------------------------')
myquery = {'ipId':1906121, 'themeCode':'RIM00119','sendTime':{'$nin':[1560412320,1560501996]}}
mydoc = mycol.find(myquery)
for doc in mydoc:
    print(doc['_id'],doc['sendTime'])

#结果计数
print('-------------结果计数------------------------------------')
myquery = {'ipId':1906121, 'themeCode':'RIM00119'}
rcount = mycol.count_documents(myquery)
print("{'ipId':1906121, 'themeCode':'RIM00119'}查询结果条数为:", rcount)

#偏移
print('-------------偏移------------------------------------')
results = mycol.find({'ipId':1906121, 'themeCode':'RIM00119'}).sort('sendTime',pymongo.DESCENDING)
for result in results:
    print('无偏移的结果',result)
results = mycol.find({'ipId':1906121, 'themeCode':'RIM00119'}).sort('sendTime',pymongo.DESCENDING).skip(10)
for result in results:
    print('有偏移的结果',result)
results = mycol.find({'ipId':1906121, 'themeCode':'RIM00119'}).sort('sendTime',pymongo.DESCENDING).skip(10)
for result in results:
    print('有偏移的结果2',result)
print(type(results))



# 插入单个文档
print('-------------插入单个文档------------------------------------')

newcol = mydb['test']
mydic = {'name':'thename', 'age':'99', 'url':'www.baidu.com'}
x = newcol.insert_one(mydic)
print('x = newcol.insert_one(mydic):', x)
print('x.acknowledged', x.acknowledged)
print('x.inserted_id', x.inserted_id)
xs = newcol.find()
for x in xs:
    print('newcol集合的数据：',x)
print('-------------插入多个文档------------------------------------')
mylist = [
    {'name': 'thename01', 'age': '01', 'url': 'www.baidu01.com'},
    {'name': 'thename02', 'age': '02', 'url': 'www.baidu02.com'}
    ]
x = newcol.insert_many(mylist)
print(x.inserted_ids)
xs = newcol.find()
for x in xs:
    print('newcol集合的数据：',x)
# print('-------------插入指定id的多个文档------------------------------------')
# mylist = [
#     {'_id': 28, 'name': 'thename08', 'age': '08', 'url': 'www.baidu08.com'},
#     {'_id': 29, 'name': 'thename09', 'age': '09', 'url': 'www.baidu09.com'}
#     ]
# x = newcol.insert_many(mylist)
# print(x.inserted_ids)
# xs = newcol.find()
# for x in xs:
#     print('newcol集合的数据：',x)

#修改
print('-------------更新一条数据------------------------------------')
myquery = {'name':'thename01'}
newvalues = {'$set':{'url':'www.update.com'}}
newcol.update_one(myquery,newvalues)
for x in newcol.find():
    print(x)
print('-------------更新所有匹配的数据------------------------------------')
myquery = {'name':'thename01'}
newvalues = {'$set':{'url':'www.all_update.com'}}
newcol.update_many(myquery,newvalues)
for x in newcol.find():
    print(x)

# 删除
print('-------------删除一个文档/数据------------------------------------')
myquery = {'name':'thename'}
count1 = newcol.estimated_document_count()
print('删除前总文档数量：', count1)
newcol.delete_one(myquery)
count2 = newcol.estimated_document_count()
print('删除后总文档数量：', count2)
for x in newcol.find():
    print(x)
print('-------------删除多个文档/数据------------------------------------')
myquery = {'name':'thename'}
count1 = newcol.estimated_document_count()
print('删除前总文档数量：', count1)
newcol.delete_many(myquery)
count2 = newcol.estimated_document_count()
print('删除后总文档数量：', count2)
for x in newcol.find():
    print(x)
print('-------------删除集合中所有文档------------------------------------')
count1 = newcol.estimated_document_count()
print('删除前总文档数量：', count1)
newcol.delete_many({})
count2 = newcol.estimated_document_count()
print('删除后总文档数量：', count2)
for x in newcol.find():
    print(x)
print('-------------删除集合------------------------------------')
print('删除集合前，所有集合列表：')
collist = mydb.list_collection_names()
for coll in collist:
    print(coll)
newcol.drop()
print('删除集合后，所有集合列表：')
collist = mydb.list_collection_names()
for coll in collist:
    print(coll)