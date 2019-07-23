#coding:UTF-8
#__autor__='wyxces'

'''
83、正则匹配以163.com结尾的邮箱
'''

import re
mails = ['ssss.aa.com',
        'ssss.vv.com',
        'ssss.qs.com',
        'ssss.qa.com',
        'ssss.123.com',
        'ssss.456.com',
        'ssss.163.com',
        'sws.163.com',
        'ssss.183.com',
        'ssqewrs.163.com'
        ]

pattern = r"163.com$"
for mail in mails:
    if re.findall(pattern,mail):
        print(mail)

'''
运行结果：
ssss.163.com
sws.163.com
ssqewrs.163.com
'''