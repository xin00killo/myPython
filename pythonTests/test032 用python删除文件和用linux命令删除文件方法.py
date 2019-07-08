#coding=utf-8
# __autor__='wyxces'

'''
用python删除文件和用linux命令删除文件方法
'''
import os

# python删除文件   os.remove(文件名)
path = 'test032.text'
with open( path, 'w+' ) as f:
    f.write('xxxxx')
    f.seek(0)
    print( f.read() )
print(path,' is  ',os.path.exists(path))
os.remove(path)
print(path,' is  ',os.path.exists(path))


#linux命令
'''
rm 文件名字
'''

