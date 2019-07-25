#coding:UTF-8
#__autor__='wyxces'


'''
85、python字典和json字符串相互转化方法
'''

'''
json数据处理	Json，全名 JavaScript Object Notation
Encode（python->json）	python里面bool值是True和False
json里面bool值是true和false,并且区分大小写
在python里面写的代码，传到json里，肯定识别不了，所以需要把python的代码经过encode后成为json可识别的数据类型
decode(json->python)	如果以content字节输出，返回的是一个字符串：{"success":true}
如果经过json解码后，返回的就是一个字典：{u'su ccess': True}

json.dumps()/json.loads()用来编码和解码json字符串数据
'''

import json

pDict = {"id": "1907194",
		"piecesNoId": "20190000000001907194",
		"upridkTime": "1560664993",
		"loanType": "315",
		"loanTime": "1",
		"cityId": "3327",
		"presonaId": "550"}
pJson = json.dumps(pDict)
print('pDict:',type(pDict),pDict)
print('pJson:',type(pJson),pJson)

pDict_new = json.loads(pJson)
print('pDict_new:',type(pDict_new),pDict_new)

'''
运行结果：
pDict: <class 'dict'> {'id': '1907194', 'piecesNoId': '20190000000001907194', 'upridkTime': '1560664993', 'loanType': '315', 'loanTime': '1', 'cityId': '3327', 'presonaId': '550'}
pJson: <class 'str'> {"id": "1907194", "piecesNoId": "20190000000001907194", "upridkTime": "1560664993", "loanType": "315", "loanTime": "1", "cityId": "3327", "presonaId": "550"}
pDict_new: <class 'dict'> {'id': '1907194', 'piecesNoId': '20190000000001907194', 'upridkTime': '1560664993', 'loanType': '315', 'loanTime': '1', 'cityId': '3327', 'presonaId': '550'}
'''
