#coding:UTF-8
#__autor__='wyxces'

import os

#os模块的方法 :2 21 28 35 45 47 49 64

#2 改变当前工作目录  21 返回当前工作目录
from _ast import arg

from Tools.scripts.findlinksto import visit

rpath = os.getcwd()
print('当前工作目录为：',rpath)
chdirpath = r'D:\code'
print('chdirpath',chdirpath)
result = os.chdir(chdirpath)
print(result)
print('chdir后的工作目录为:',os.getcwd())

#28 返回path指定的文件夹包含的文件或文件夹的名字的列表。
path = os.getcwd()
print('当前目录：%s下 文件夹/文件的目录列表：\n\t%s'%(path,os.listdir(path)))
# os.chdir(rpath)
# path = os.getcwd()
# print('当前目录：%s文件夹下 文件夹/文件的目录列表：\n\t%s'%(path,os.listdir(path)))

#35以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
mkdirpath='wyxcesmkdirpath'
print('在当前工作目录下创建一个新文件夹：',mkdirpath)
try:
    os.mkdir(mkdirpath)
except FileExistsError:
    print('%s文件已存在，创建失败'%mkdirpath)
print('%s创建后，当前目录：%s下 文件夹/文件的目录列表：\n\t%s'%(mkdirpath,os.getcwd(),os.listdir(path)))

# 45 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory
# 46 递归删除目录。
# 49 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
# 49 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
# 45
# 准备工作： 创建用来删除 一个的txt文件、一个空文件夹 、一个非空文件夹
print('\n准备工作： 创建用来删除 一个的txt文件、一个空文件夹 、一个非空文件夹')
txtFile = r'D:\code\wyxcesTxtFile.txt'
emptyFolder = 'wyxcesEmptyFolder'
nonEmptyFolders = r'wyxcesNonEmptyFolder\nonEmptyFolder'
nonEmptyFolder = r'wyxcesNonEmptyFolder'
print('如果不存在，则创建一个的txt文件:',txtFile)
f = open(txtFile,'w')
f.close()
try:
    print('创建一个空文件夹:', emptyFolder)
    os.mkdir(emptyFolder)
except FileExistsError:
    print('文件%s已存在，创建失败'%emptyFolder)

try:
    print('创建一个非空文件夹:', nonEmptyFolders)
    os.makedirs(nonEmptyFolders)
except FileExistsError:
    print('文件%s已存在，创建失败'%nonEmptyFolders)

print('准备工作完成后，当前目录：%s下 文件夹/文件的目录列表：\n\t%s'%(os.getcwd(),os.listdir(path)))

try:
    print('\nos.remove() 删除txt文件:', txtFile)
    os.remove(txtFile)
    print('os.remove()后，当前目录：%s下 文件夹/文件的目录列表：\n\t%s' % (os.getcwd(), os.listdir(path)))
except BaseException as f:
    print('os.remove(%s)'%txtFile,f)

try:
    print('\nos.remove() 删除目录文件:', emptyFolder)
    os.remove(emptyFolder)
    print('os.remove()后，当前目录：%s下 文件夹/文件的目录列表：\n\t%s'% (os.getcwd(), os.listdir(path)))
except BaseException as f:
    print('os.remove %s)'%emptyFolder,f)

try:
    print('\nos.rmdir() 删除非空目录文件:', nonEmptyFolder)
    os.rmdir(nonEmptyFolder)
    print('os.rmdir()后，当前目录：%s下 文件夹/文件的目录列表：\n\t%s'% (os.getcwd(), os.listdir(path)))
except BaseException as f:
    print('os.rmdir(%s)'%nonEmptyFolder,f)

try:
    print('\nos.rmdir() 删除空目录文件:', emptyFolder)
    os.rmdir(emptyFolder)
    print('os.rmdir()后，当前目录：%s下 文件夹/文件的目录列表：\n\t%s'% (os.getcwd(), os.listdir(path)))
except BaseException as f:
    print('os.rmdir(%s)'%emptyFolder,f)

try:
    print('\nos.removedirs() 删除非空目录文件:', nonEmptyFolder)
    os.removedirs(nonEmptyFolder)
    print('os.removedirs()后，当前目录：%s下 文件夹/文件的目录列表：\n\t%s'% (os.getcwd(), os.listdir(path)))
except BaseException as f:
    print('os.removedirs(%s)'%nonEmptyFolder,f)

# 47 重命名文件或目录，从 src 到 dst
srcName = r'wyxcesmkdirpath'
dstName = 'wyxcesmkdirpath_dstName'
try:
    print('\n将 %s 文件 重命名为 %s '%(srcName,dstName))
    os.rename(srcName,dstName)
    print('os.rename()后，当前目录：%s下 文件夹/文件的目录列表：\n\t%s' % (os.getcwd(), os.listdir(path)))
except FileExistsError as f:
    print('os.rename(%s  到  %s)'%(srcName,dstName),f)

os.chdir(rpath)
# 64 获取文件的属性信息。 os.path 模块
print('\n --------------os.path 模块学习 --------------')
file = 'files/os.txt'  # 文件的相对路径
fileAllPath = r'D:\code\myPython\basic\os_\os.txt'
#返回绝对路径
print('wyxcesmkdirpath的绝对路径为：%s'%(os.path.abspath('wyxcesmkdirpath')))
print('file：%s的绝对路径为：%s'%(file,os.path.abspath('file')))
#返回文件名
fileName = os.path.basename(file)
print('%s 的文件名为：%s'%(file,fileName))
#返回文件路径
filePath = os.path.dirname(file)
print('%s 的文件路径：%s'%(file,filePath))
#路径存在则返回True,路径损坏返回False
path1 = 'E:\learn\pythonCode\wyxces'
path2 = 'E:\learn\pythonCode\wyxces9'
path3 = 'E:\learn\pythonCode\wyxces\hello.py'
print('路径%s存在？'%path1,os.path.exists(path1))
print('路径%s存在？'%path2,os.path.exists(path2))
print('路径%s存在？'%path3,os.path.exists(path3))
#返回最近文件修改时间 \ 创建时间 \修改时间
try:
    print('%s的最近修改时间为：%s'%(file,os.path.getmtime(file)))
except BaseException as f:
    print('os.path.getmtime(%s)'%file,f)
try:
    print('%s的创建时间为：%s'%(file,os.path.getctime(file)))
except BaseException as f:
    print('os.path.getctime(%s)'%file,f)
print('%s的最近修改时间为：%s'%(fileAllPath,os.path.getmtime(fileAllPath)))
print('%s的创建时间为：%s'%(fileAllPath,os.path.getctime(fileAllPath)))
print('%s的修改时间为：%s'%(fileAllPath,os.path.getatime(fileAllPath)))
# 返回文件大小，如果文件不存在就返回错误
try:
    print('文件%s的大小为：%s'%(file,os.path.getsize(file)))
except BaseException as f:
    print('os.path.getsize(%s)'%file,f)
print('文件%s的大小为：%s'%(fileAllPath,os.path.getsize(fileAllPath)))
# 判断是否为绝对路径
print('%s 是否为绝对路径：%s'%(file,os.path.isabs(file)))
print('%s 是否为绝对路径：%s'%(fileAllPath,os.path.isabs(fileAllPath)))
#判断路径是否为文件
print('%s 是否为文件：%s'%(file,os.path.isfile(file)))
print('%s 是否为文件：%s'%(fileAllPath,os.path.isfile(fileAllPath)))
#判断路径是否为目录
path4 = 'files/file2'
print('%s 是否为目录：%s'%(file,os.path.isdir(file)))
print('%s 是否为目录：%s'%(fileAllPath,os.path.isdir(fileAllPath)))
print('%s 是否为目录：%s'%(path1,os.path.isdir(path1)))
print('%s 是否为目录：%s'%(path4,os.path.isdir(path4)))
# 判断路径是否为链接
url = 'https://www.runoob.com/python3/python3-os-path.html'
link1 = 'E:\learn\pythonCode\wyxces\\files\\files.lnk'
link2 = 'files/files.lnk'
print('%s 是否为链接：%s'%(file,os.path.islink(file)))
print('%s 是否为链接：%s'%(url,os.path.islink(url)))
print('%s 是否为链接：%s'%(link1,os.path.islink(link1)))
print('%s 是否为链接：%s'%(link2,os.path.islink(link2)))
# 把目录和文件名合成一个路径
joinPath = os.path.join(filePath,fileName)
print('将目录%s和文件名%s合成一个路径为：%s'%(filePath,fileName,joinPath))
# 返回path的真实路径
fileRealPath = os.path.realpath(file)
print('当前工作目录：',os.getcwd())
print('%s 的真实路径：%s'%(file,fileRealPath))
os.chdir(chdirpath)
print('如果切换了工作目录到%s，则%s的真实路径会变成：%s'%(os.getcwd(),file,os.path.realpath(file)))
os.chdir(rpath)
print('%s 的真实路径：%s'%(link1,os.path.realpath(link1)))
#判断目录或文件是否相同
# try:
#     print('%s和%s是否相同：%s'%(link1,link2,os.path.samefile(link1,link2)))
# except FileNotFoundError as f :
#     print('samefile(%s,%s)'%(link1,link2),f)
# comparePath = r'E:\learn\pythonCode\wyxces\files\files.lnk'
# print('%s和%s是否相同：%s'%(comparePath,link1,os.path.samefile(comparePath,link1)))
# 把路径分割成 dirname 和 basename，返回一个元组
print('把路径%s分割成dirname和basename:%s'%(fileRealPath,os.path.split(fileRealPath)))
print('把路径%s分割成dirname和basename:%s'%(file,os.path.split(file)))
# 分割路径，返回路径名和文件扩展名的元组
print('路径%s分割成路径名和文件扩展名:%s'%(file,os.path.splitext(file)))
# 把路径分割为加载点与文件
try:
    print('路径%s分割成加载点与文件:%s'%(file,os.path.splitunc(file)))
except AttributeError as f :
    print('os.path.splitunc(file)',file,f)
try:
    print('路径%s分割成加载点与文件:%s'%(rpath,os.path.splitunc(rpath)))
except AttributeError as f :
    print('os.path.splitunc(rpath)',rpath,f)
'''
遍历path，进入每个目录都调用visit函数，
visit函数必须有3个参数(arg, dirname, names)，
dirname表示当前目录的目录名，
names代表当前目录下的所有文件名，
args则为walk的第三个参数
'''
# print('os.path.walk(path, visit, arg)',path,os.path.walk(path, visit, arg))
try:
    print('os.path.walk(path, visit, arg)'%(file,os.path.walk(file)))
except AttributeError as f :
    print('os.path.walk(file)',file,f)
try:
    print('os.path.walk(path, visit, arg)'%(rpath,os.path.walk(rpath)))
except AttributeError as f :
    print('os.path.walk(rpath)',rpath,f)