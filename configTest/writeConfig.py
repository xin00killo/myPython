# coding:UTF-8
# __autor__ = 'wyxces'

import configparser



cf = configparser.ConfigParser()
path = r'D:\code\myPython\configTest\config.ini'
cf.read(path)
cf.set('PATH', 'path', '999')
cf.write(open(path, "w"))