#coding=utf-8
# __autor__='wyxces'

'''
使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
'''

dic1={"name":"zs","age":18}
dic1.pop('name')
print(dic1)

dic2={"name":"zs","age":18}
del dic2["name"]
print(dic2)