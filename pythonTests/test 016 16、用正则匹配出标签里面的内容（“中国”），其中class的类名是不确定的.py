#coding=utf-8
# __autor__='wyxces'

'''
16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的

'''
import re

str = '<div class="nam">中国</div>'

pattern =  r'<div class=".*">(.*?)</div>'

result = re.findall(pattern,str)

print('匹配结果为：', result[0])