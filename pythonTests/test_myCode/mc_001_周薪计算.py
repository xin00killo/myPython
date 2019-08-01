#coding:UTF-8
#__autor__='wyxces'


'''
一个雇员一周的总薪水，等于其每小时的时薪，乘以其一周工作的正常小时数，
再加上加班费。加班费等于总的加班时间，乘以每小时薪水的1.5倍。
编写一个程序，以每小时的薪水，常规工作时间，加班工作时间作为参数，显示一个雇员的总周薪。
'''

'''
分析
用户输入：每小时的薪水，常规工作时间(本周)，加班工作时间
需要计算的数据：
    正常工作薪资：时薪*常规工作时间
    加班费：加班时间*时薪*1.5
    周薪= 正常工作薪资 + 加班费

类：员工薪资类
方法：薪资计算、返回结果、用户输入
'''
import  re
def weekSalary():
    # weekly wage/salary 周新
    #  hourly wage 时薪
    hourlyWage = userInput("hourlyWage")
    # Routine working hours 常规工作时间
    routineWorkingHours = userInput("routineWorkingHours")
    # Overtime hours 加班时长
    overtimehHours = userInput("overtimehHours")
    routineWages = round(hourlyWage * routineWorkingHours,2)
    overtimePay = round(hourlyWage*1.5*overtimehHours,2)
    weekSalary = routineWages + overtimePay
    print("该员工总薪资为：{}，其中:\n\t常规工时{}小时薪资为：{}\n\t加班工时{}小时薪资为：{}".format(weekSalary,routineWorkingHours,routineWages,overtimehHours,overtimePay))

def userInput(type):
    if type == "hourlyWage":
        hw = input("请输入时薪：")
        partten = r"^[\+-]?\d+$|^[\+-]?\d+\.?\d+$" # 整数 或 小数
        if not re.findall(partten,hw) or float(hw)<= 0 :
            print("时薪应为不小于0的数字，请重新输入。。。。")
            return userInput("hourlyWage")
        return float(hw)
    elif type == "routineWorkingHours":
        rwh = input("请输入本周常规工作时长：")
        partten = r"^[\+-]?\d+$" # 整数
        if not re.findall(partten,rwh) or int(rwh)>40 or int(rwh)<0 :
            print("周工作时间应为0-40的整数，请重新输入。。。。")
            return userInput("routineWorkingHours")
        return int(rwh)
    elif type == "overtimehHours":
        oh = input("请输入本周加班时长：")
        partten = r"^[\+-]?\d+$" # 整数
        # print(re.findall(partten,oh),oh)
        if not re.findall(partten,oh) or int(oh)<=0 :
            print("加班时长需为不小于0的整数，请重新输入。。。。")
            return userInput("overtimehHours")
        return int(oh)

# userInput("overtimehHours")

weekSalary()

"""
运行结果：
请输入时薪：986.5
请输入本周常规工作时长：38
请输入本周加班时长：15
该员工总薪资为：59683.25，其中:
	常规工时38小时薪资为：37487.0
	加班工时15小时薪资为：22196.25
"""