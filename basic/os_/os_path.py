#coding=utf-8
# __autor__='wyxces'

import os
test_path = os.getcwd()
print("test_path",test_path)
file_name = "os_.py"
print("file_name",file_name)

# 返回绝对路径
print("abspath",os.path.abspath(test_path))
# 返回文件名
print("basename",os.path.basename(test_path))
# 返回文件路径
print("dirname",os.path.dirname(test_path))
# 路径存在则返回True,路径损坏返回False
print("exists",os.path.exists(test_path))
# 返回最近文件修改时间
print("getmtime",os.path.getmtime(test_path))
# 返回文件 path 创建时间
print("getctime",os.path.getctime(test_path))
# 返回文件大小，如果文件不存在就返回错误
print("size",os.path.getsize(test_path))
# 判断是否为绝对路径
print("isabs",os.path.isabs(test_path))
# 判断路径是否为文件
print("isfile",os.path.isfile(test_path))
# 判断路径是否为目录
print("isdir",os.path.isdir(test_path))
# 判断路径是否为链接
print("islink",os.path.islink(test_path))
# 把目录和文件名合成一个路径
file_path = os.path.join(test_path,file_name)
print("file_path",file_path)
# 返回path的真实路径
print("realpath",os.path.realpath(test_path))
'''
files/os.txt 的真实路径：D:\code\myPython\basic\os_\files\os.txt
如果切换了工作目录到D:\code，则files/os.txt的真实路径会变成：D:\code\files\os.txt
'''
# 判断目录或文件是否相同
file_name2 = "f.txt"
print("samefile",os.path.samefile(file_name,file_name))
print("samefile",os.path.samefile(file_name,file_name2))
# 把路径分割成 dirname 和 basename，返回一个元组
print("split",os.path.split(file_path))
# 分割路径，返回路径名和文件扩展名的元组
print("splitext",os.path.splitext(file_path))
# 遍历path，进入每个目录都调用visit函数，
# visit函数必须有3个参数(arg, dirname, names)，
# dirname表示当前目录的目录名，
# names代表当前目录下的所有文件名，
# args则为walk的第三个参数

