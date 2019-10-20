#coding=utf-8
# __autor__='wyxces'

from  appiumUI.common.read_config import Driver,getCFObj
import  appiumUI.common.read_config
d = Driver()
cf = getCFObj()
print(cf)
d.platform_name