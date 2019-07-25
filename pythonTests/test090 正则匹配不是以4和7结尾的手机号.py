#coding:UTF-8
#__autor__='wyxces'


'''
90、正则匹配不是以4和7结尾的手机号
'''
import re

phones = [
    12345678945,
    45943146423,
    464414231414,
    4859642546,
    4567924674874,
    48761431154,
    41122336642,
    122359984,
    142365991457,
    12368476367,
    13969845679
]
# [直接简化匹配结尾数字了，不管是不是手机号]
pattern = r'[^47]$'
new_phones = []
for p in phones:
    if re.findall(pattern,str(p)):
        new_phones.append(p)
print(new_phones)
