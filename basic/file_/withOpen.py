#coding=utf-8
# __autor__='wyxces'

#读
with open('myfile.text', 'r', encoding='utf-8') as fr :
    print(fr.read())


#写
with open('myfile.text', 'w', encoding='utf-8') as fw:
    fw.write('''hello world! by wyx 12345678901234567890
    hello world! by wyx 1234567890
    hello world! by wyx 123456789012345678901234567890
    hello world! by wyx 1234567890123456789012345678901234567890
    hello world! by wyx 12345678901234567890123456789012345678901234567890
    ''')

