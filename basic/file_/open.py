#coding=utf-8
# __autor__='wyxces'

# 打开一个文件的方法
f = open('myFile.text', 'a+', encoding='UTF-8')
# 读写文件的模式
'''
r 只读,光标置于文件头
r+ 读写，光标置于文件头,在头部替换写入（insert选中了那种键盘写入）
w 只写
w+ 读写，覆盖写入，如果没有文件，则新建
a 只写，光标位置文件末尾，追加写入,如果没有文件，则新建
a+ 读写，光标位于未见末尾，追加写入，如果没有文件，则新建
'''
#读取指定字节数的文件
str = f.read(15)
print('read 15:', str)

#按指定字符数，读取整行（包括\n）
f.seek(0)
str = f.readline(9)
print('readline 9:',str)
f.seek(0)
str = f.readline(39)
print('readline 39:',str)

#读取所有行，并返回列表
f.seek(0)
myList = f.readlines()
print('readlines',type(myList),'\n',myList)
for line in myList:
    print(line)

#移动光标位置
f.seek(0)

#返回当前文件 位置
tell = f.tell()
print('tell:', tell)
f.read(16)
tell = f.tell()
print('read 16 --> tell:', tell)

#将字符写入文件
f2 = open('myFile.text', 'r+')
f2.write('/1231open-write1232324234234/')
f.write('/ffff-write1ffff/')


#将一个序列字符串列表写入文件
seq = ['aaa','215646','156941','erq3gsdag数据','\n156']
f.writelines(seq)

#关闭文件
f.close()
f2.close()