#coding=utf-8
# __autor__='wyxces'
import os

from appiumUI.common.public import singleton
from appiumUI.common.read_config import R_Driver
from appium import webdriver

os.chdir(os.path.dirname(os.getcwd()))


@singleton
class Driver():
    def startUP(self):
        rd = R_Driver()
        dc = { #desired_capabilities
            "platformName":  rd.getValue("platformName"),
            "deviceName":  rd.getValue("deviceName"),
            "platformVersion":  rd.getValue("platformVersion"),
            # "app": rd.getValue("app"),
            "appPackage":  rd.getValue("appPackage"),
            "appActivity":  rd.getValue("appActivity"),
            "noReset":  rd.getValue("noReset")
        }
        self.driver = webdriver.Remote( rd.getValue("command_executor"),desired_capabilities=dc)
        return self.driver  #添加上self. 后，当前class的其他方法，可以直接调用

@singleton
class Driver2():
    rd = R_Driver()
    dc = { #desired_capabilities
        "platformName":  rd.getValue("platformName"),
        "deviceName":  rd.getValue("deviceName"),
        "platformVersion":  rd.getValue("platformVersion"),
        # "app": rd.getValue("app"),
        "appPackage":  rd.getValue("appPackage"),
        "appActivity":  rd.getValue("appActivity"),
        "noReset":  rd.getValue("noReset")
    }
    driver = webdriver.Remote( rd.getValue("command_executor"),desired_capabilities=dc)



if __name__ == "__main__":
    print("当前目录", os.getcwd())
    os.chdir(os.path.dirname(os.getcwd()))
    print("工作目录", os.getcwd())
    driverObj1 = Driver2()
    driver1 = driverObj1.driver
    print("1",driverObj1,driver1)
    driverObj2 = Driver2()
    driver2 = driverObj2.driver
    print("2", driverObj2,driver2)