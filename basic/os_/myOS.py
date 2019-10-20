#coding=utf-8
#__author__='wyx'

import os,sys,stat,shutil

path='D:\code\VIPtest2\MyPractice/os.txt'

print('path:',path)

#权限查询
print('os.access(path,os.F_OK):',os.access(path,os.F_OK))
print('os.access(path,os.R_OK):',os.access(path,os.R_OK))
print('os.access(path,os.W_OK):',os.access(path,os.W_OK))
print('os.access(path,os.X_OK):',os.access(path,os.X_OK))

print('\n\n')
#工作目录
#查看当前工作目录
oldPath=os.getcwd()
print('当前工作目录oldPath:',oldPath)
#修改当前工作目录
newPath='D:/code/VIPtest2/'
print('想要修改工作目录到newPath:',newPath)
os.chdir(newPath)
print('修改工作目录os.chdir(newPath)后，再次获取当前工作目录:',os.getcwd())
os.chdir(oldPath)
print('再次修改os.chdir(oldPath)工作目录后，获取当前工作目录:',os.getcwd())

#权限更改
os.chmod(path,stat.S_IRWXU)
#更改所有者
# os.chown(path,-1,100)  #貌似仅unix下可用啊  AttributeError: module 'os' has no attribute 'chown'
print('\n\n')
#复制文件描述符  打开文件
f=os.open("f.txt",os.O_RDWR|os.O_CREAT)  #打开文件，读写权限，创建文件
print('f',f)
len=os.write(f,'这里是f写入\n'.encode()) #使用文件描述符写入文件
print('len 写入的字符串长度为',len)
f_dup=os.dup(f) #复制文件描述符
print('f_dup',f_dup)
os.write(f_dup,'这里是f_dup写入\n'.encode()) #使用复制的文件描述符写入文件
f_dup2=os.dup(f) #复制文件描述符
print('f_dup2',f_dup2)
os.write(f_dup2,'这里是f_dup2写入\n'.encode()) #使用复制的文件描述符写入文件


#通过文件操作符更改目录
# print('当前工作目录为：',os.getcwd())
# os.fchdir(f)       ####  只有在unix下才能用
# print('当前工作目录为：',os.getcwd())
print('\n\n')
#打开文件  写入信息
fd=os.open(path,os.O_RDWR|os.O_CREAT|os.O_APPEND)
print('fd=%d,fd=os.open(path,os.O_RDWR|os.O_CREAT|os.O_APPEND)'%fd)
os.write(fd,'\n用os.write方法，f2文件操作符，写入追加写入信息？'.encode())
fo=os.fdopen(fd,'a+') #获取以上文件的对象
os.write(fd,'''\nfo=os.fdopen(f2,'a+')'''.encode())
#获取当前文章？
print('当前I/O标志的位置',fo.tell())
#写入字符串
fo.write('\nfo.write  写入字符串 ')
# 设置文件标识符位置到文件开头
os.lseek(fd,0,0)
#读取内容
str=os.read(fd,100)
print('读取内容str=os.read(fd,100):',str)
#获取当前位置
print('当前i/O 标志的位置',fo.tell())
print('fd:',fd)
print('fo:',fo)

print('\n\n')
# print('getcwdu',os.getcwdu())   AttributeError: module 'os' has no attribute 'getcwdu'
#返回文件描述符的状态
osfstat=os.fstat(fd)
print('fd文件描述符状态信息fstat:',osfstat)
print('fd文件描述符的uid',osfstat.st_uid)
#返回path指定文件夹包含的文件/文件夹名字的列表
print('path：%s下的列表%s:'%(newPath,os.listdir(newPath)))
#返回当前工作目录
print('getcwd:',os.getcwd())
pythonCodePath='D:\code\VIPtest2/MyPractice'
os.chdir(pythonCodePath)
print('切换工作目录到python代码目录：',os.getcwd())
print('当前的工作目录为：',os.getcwd())

print('\n\n')
# 想要创建目录的路径
mkdirpath='/myMkdir'
#删除空目录
try:
    os.rmdir(mkdirpath)
except BaseException:
    pass
##创建目录
os.mkdir(mkdirpath)
os.chdir(mkdirpath)
print('切换目录到新建的 mkdirpath="/myMkdir"后，当前目录为：',os.getcwd())
os.chdir(pythonCodePath)
print('切换工作目录到python代码目录后，当前目录为：',os.getcwd())

print('\n\n')
#从文件标识符中读取n给字节
fdr=os.open(path,os.O_RDWR)
print('从文件标识符中读取n给字节os.read(fdr,10):',os.read(fdr,10))
# fd=os.open(path,os.O_RDWR|os.O_CREAT|os.O_APPEND)
os.lseek(fd,0,0)
print('从文件标识符中读取n给字节os.read(fd,10):',os.read(fd,10))
print('fdr',fdr)

print('\n\n')
#重命名   将文件重命名
#在 MyPractice 下新建一个目录，myRenames   目录下 新建一个文件 myRenames.txt
# try:  #这个目录将来会是非空的，会出错 不能用这个方法哈
#     os.removedirs('myRenames')
#     print(os.removedirs('myRenames'))
# except BaseException:
#     raise
try:
    shutil.rmtree('myRenames')
except:
    pass
print('当前目录为：',os.getcwd())
print('目录列表\n\t',os.listdir(os.getcwd()))
os.mkdir('myRenames')
print('os.mkdir(myRenames)后目录列表\n\t',os.listdir(os.getcwd()))
fdmr=os.open('myRenames/myRenames.txt',os.O_RDWR|os.O_CREAT)
os.close(fdmr)
print('myRenames重命名前，目录列表：',os.listdir('myRenames'))
print('为myRenames.txt 文件重命名 为 myRenamesNew.txt')
os.renames('myRenames/myRenames.txt','myRenames/myRenamesNew.txt')
print('myRenames重命名后，目录列表：',os.listdir('myRenames'))

print('\n\n')
#设置访问和修改时间
print('os 文件原本的访问和修改时间分别为：',os.stat(path).st_atime,os.stat(path).st_mtime)
print('修改两个时间分别为  11111  222222')
os.utime(path,(11111,222222))
print('os 文件修改后的访问和修改时间分别为：',os.stat(path).st_atime,os.stat(path).st_mtime)
print('修改两个时间分别为   1558106824.4209628 1558106824.409601')
os.utime(path,(1558106824.4209628,1558106824.409601))
print('os 文件修改后的访问和修改时间分别为：',os.stat(path).st_atime,os.stat(path).st_mtime)

print('\n\n')
#写入文件
# fd=os.open(path,os.O_RDWR|os.O_CREAT|os.O_APPEND)
str='\nos.write方法写入数据'
ret=os.write(fd,bytes(str,'UTF-8'))
print('写入位数为：',ret)




os.closerange(f,fdr)


