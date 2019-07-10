#coding:UTF-8
#__autor__='wyxces'

#py3中创建 bytes类型的数据

b1 = bytes([1,2,3,4,5])
b2 = bytes('python','ascii') # 字符串，编码
print(b1,type(b1))
print(b2,type(b2))


# 字符串 转码 bytes
str = 'abcdefghijklmn'
print('str:',type(str),' ',str)
bstr1 = str.encode(encoding='utf-8')
print('bstr:',type(bstr1),' ',bstr1)

bstr2 = str.encode(encoding='gb2312')
print('bstr:',type(bstr2),' ',bstr2)

# bytes 解码 string
str1 = bstr1.decode()  # utf-8  默认解码
print('bstr:',type(str1),' ',str1)
str2 = bstr2.decode('gb2312')
print('bstr:',type(str2),' ',str2)



