#coding=utf-8
# __autor__='wyxces'

from operator import  *

'''
24、字典根据键从小到大排序
dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"
'''


mydict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}


def mysort(flist):
    length = len(flist)
    for i in range(length-1):
        for j in range(i+1,length):
            if gt(flist[i],flist[j]):
                temp = flist[i]
                flist[i] = flist[j]
                flist[j] = temp
    # print('list',list)
    return flist

def fun(dict):
    keys = list(dict.keys())
    # print(keys,type(keys))
    # keys= sorted(keys)
    # keys.sort()
    keys = mysort(keys)
    # print(keys)
    newdict = {}
    for key in keys:
        # print(key,dict[key])
        newdict[key] = dict[key]
    print('按key值排序后的字典为：',newdict)



fun(mydict)
