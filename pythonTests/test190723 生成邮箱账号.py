#coding:UTF-8
#__autor__='wyxces'



'''
你是一个高级测试工程师，现在要做性能测试，
需要你写一个函数，批量生成一些注册使用的账号。
产生的账号是以@163.com结尾，长度由用户输入，产生多少条也由用户输入，
用户名不能重复，用户名必须由大写字母、小写字母、数字组成，结果如下图：
'''
import random
import re
import string


def getMail():
    #长度、条数输入
    print('请输入邮箱长度')
    l = getInput("l")
    print("请输入需要产生邮箱的条数")
    n = getInput("n")
    # 生成邮箱
    mails = []
    i = 0
    while(i != n):
        # 随机出字符串
        mail = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(l)])
        # print(mail,re.search(r'[A-Z]',mail),re.search(r'[a-z]',mail),re.search(r'[1-9]',mail))
        # 判断是否已存在
        if mail in mails:
            continue
        # 判断是否满足 由大写字母、小写字母、数字组成
        elif not (re.search(r'[A-Z]',mail) and re.search(r'[a-z]',mail) and re.search(r'[1-9]',mail)):
            continue
        else:
            mail = mail + "@163.com"
            mails.append(mail)
            i += 1
    return mails


def getInput(type="999"):
    result = input(':')
    if re.findall(r'\D',result):
        print("输入非法，请重新输入正整型数字")
        return getInput()
    elif type == "l" and (int(result) < 3 or int(result) > 30):
        print("邮箱长度需至少3位，请重新输入3~30间的整数")
        return getInput("l")
    return int(result)




mailList = getMail()
print(mailList)