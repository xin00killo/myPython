# coding:UTF-8
# __autor__ = 'wyxces'

import configparser,os

conf = configparser.ConfigParser()
configPath = os.path.dirname(__file__) + '/config.ini'
print('configPath',configPath)
conf.read(configPath, encoding='utf-8')


# 获取文件内所有的sections
mySections = conf.sections()
print('获取文件内所有的sections', mySections)

# 获取xx section下的所有 options
myOptions = conf.options('EMAIL')
print('获取xx section下的所有 options', myOptions)

# 获取xx section下的素有键值对
myItems = conf.items('PATH')
print('获取xx section下的素有键值对', myItems)

#获取