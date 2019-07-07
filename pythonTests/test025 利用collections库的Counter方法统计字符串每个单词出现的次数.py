#coding=utf-8
# __autor__='wyxces'


'''
25、利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
'''
from collections import Counter
str = 'kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h'

c = Counter(str)
print(c)
for k,v in dict(c).items():
    print('单词{}出现的次数为:{}'.format(k,v))