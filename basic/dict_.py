#coding:UTF-8
#__autor__='wyxces'

'''
字典
dict={key:value,key:value}
s={'a':10,'b':20,'c':15}无序，不能通过下标引用，只能通过key值查出value值
当key不存在时，即添加   如果存在=修改
'''

#定义字典
mydict={"id": "1906141",
		"upridkTime": "1557995895",
		"loanType": "315",
		"loanTime": "1",
		"cityId": "3327"}
print('原字典信息为：\n\t',mydict)

#字典的操作方法
# 取出所有的key值
allkeys = mydict.keys()
print('取出所有的key值：\n\t', allkeys)

# 取出所有的value值
allvalues = mydict.values()
print('取出所有的 values 值：\n\t', allvalues)

# 取出所有的键值对，作为一个元组的元素
allitems = mydict.items()
print('取出所有的 key\\value 值：\n\t', allitems)
print('遍历key value：')
for key, value in mydict.items():
    print('\t',key, value)

# 合并两个字典
mydict2 = {"pb_sf_qry_6m" : 1,
		    "pb_org_qry_loan_1m" : 0,
		    "pb_ln_car_ct_new3m" : -99,
		    "pb_ln_cons_npfm_ct_2y" : 0}
print('第二个字典的信息为：\n\t', mydict2)
mydict.update(mydict2)
print('mydict与mydict2合并后的字典信息为：\n\t',mydict)

# 删除key
del mydict['loanTime']
print('删除 loanTime 后的字典信息为：\n\t',mydict)

# 清空字典
mydict.clear()
print('clear后的字典信息为：\n\t',mydict)

