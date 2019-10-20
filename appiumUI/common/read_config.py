#coding=utf-8
# __autor__='wyxces'

import os

import configparser
from appiumUI.common.public import singleton

cf_obj = configparser.ConfigParser() #使得只创建一个cf对象
# print(cf_obj)
def getCFObj(*args, **kwargs):
    cf_path = r"config.ini"  #文件路径
    # print(os.path.abspath(config_path))
    cf_obj.read(cf_path,encoding="utf-8-sig") #读取文件
    return cf_obj

@singleton
class R_Driver():
    def __init__(self):
        self.cf = getCFObj()
        # self.cf2 = getConfigObj()
        # print(self.cf,"\n",self.cf2)
        self.platformName = self.getValue("platformName")
        self.deviceName = self.getValue("deviceName")
        self.platformVersion = self.getValue("platformName")
        self.app = self.getValue("app")
        self.appPackage = self.getValue("appPackage")
        self.appActivity = self.getValue("appActivity")
        self.noReset = self.getValue("noReset")
    def __str__(self):
        print(self.platformName,
        self.deviceName,
        self.platformVersion,
        self.app,
        self.appPackage,
        self.appActivity,
        self.noReset)
    def getValue(self,name):
        return self.cf.get("driver",name)








if __name__ == "__main__":
    print("当前目录",os.getcwd())
    os.chdir(os.path.dirname(os.getcwd()))
    print("工作目录",os.getcwd())

    d = R_Driver()
    d.__str__()