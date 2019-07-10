#coding:UTF-8
#__autor__='wyxces'

'''
46 a="hello"和b="你好"编码成bytes类型
'''

a="hello"
b="你好"
print('a:',type(a),a)
print('b:',type(b),b)


ba8 = a.encode('utf-8')
bb8 = b.encode('utf-8')
print('ba8:',type(ba8),ba8)
print('bb8:',type(bb8),bb8)


ba2312 = a.encode('gb2312')
bb2312 = b.encode('gb2312')
print('ba2312:',type(ba2312),ba2312)
print('bb2312:',type(bb2312),bb2312)


'''
a: <class 'str'> hello
b: <class 'str'> 你好
ba8: <class 'bytes'> b'hello'
bb8: <class 'bytes'> b'\xe4\xbd\xa0\xe5\xa5\xbd'
ba2312: <class 'bytes'> b'hello'
bb2312: <class 'bytes'> b'\xc4\xe3\xba\xc3'
'''