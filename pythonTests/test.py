#coding=utf-8
# __autor__='wyxces'


import  re
str = 'href="Products.aspx?page=0&amp;categoryId=BIRDS">Birds</a>'

news = re.findall(r'categoryId=.*?\">(.*?)</a>',str)
print(news)