#coding=utf-8
# __autor__='wyxces'

import os

#  --权限检测
file_path = r"D:\code\myPython\basic\file_\myFile.text"
work_path = r"D:\code\myPython\basic\file_"
# 是否存在
print(os.access(path=file_path,mode=os.F_OK))
# 是否可读
print(os.access(path=file_path,mode=os.R_OK))
# 是否可写
print(os.access(path=file_path,mode=os.W_OK))
# 是否可执行
print(os.access(path=file_path,mode=os.X_OK))

# 获取当前目录
org_path = os.getcwd()
print(org_path)
# 修改工作目录
os.chdir(work_path)
print(os.getcwd())
os.chdir(org_path)
#   --打开文件
'''
# 以只读方式打开
os.open(file=file_path,flags=os.O_RDONLY)
# 只写
os.open(file=file_path,flags=os.O_WRONLY)
# 读写
os.open(file=file_path,flags=os.O_RDWR)
# 打开时不阻塞
# os.open(file=file_path,flags=os.O_NOINHERIT)
# 追加
os.open(file=file_path,flags=os.O_APPEND)
# 创建并打开一个新文件
os.open(file_path,flags=os.O_CREAT)
# 打开一个文件并截断它的长度为0
os.open(file_path,flags=os.O_TRUNC)
# 如果指定的文件存在，则返回错误
os.open(file_path,flags=os.O_EXCL)
'''
# 设置描述符fd当前位置为 pos how
# 文件头

# 当前位置
#
# 末尾

# 返回path指定文件夹包含的文件/文件夹名字的列表
print(os.listdir(org_path))
# 创建目录
mk_path=org_path+"\mkdir1"
mk_path2=org_path+"\mkdir2"
try:
    os.mkdir(path=mk_path,mode=1)
    os.mkdir(path=mk_path2, mode=1)
except Exception as e:
    print(e)
print(os.listdir(org_path))
# 递归创建文件目录
mks_path = org_path+"\mks"+"\dirs"
try:
    os.makedirs(mks_path,1)
except Exception as e:
    print(e)
print(os.listdir(org_path))
# 删除空目录
os.rmdir(mk_path)
print(os.listdir(org_path))
# 递归删除目录
os.removedirs(mks_path)
print(os.listdir(org_path))
# 删除路径为path的文件

# 删除一个文件

# 读取n个字节

# 重命名
try:
    re_names = "renames"
    os.renames(mk_path2, re_names)
except Exception as e:
    print(e)

# os.rename()
try:
    re_names = "renames"
    os.rename(mk_path2, re_names)
except Exception as e:
    print(e)
# 设定访问和修改的时间
