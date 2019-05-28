#coding:UTF-8
#__autor__='wyxces'

import requests

class RequestJson:
    def requestJsonKuaidi(self):
        url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-3710282746981-shentong.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
        }
        s = requests.session()
        r = s.get(url= url, headers=headers, verify= False)
        result = r.json()
        print('result = r.json()',result)
        result2 = r.content
        print('result2 = r.content', result2)
        # param = {
        #     'geetest_validate': 'd5305e4eae689b3ea4715c0f68bac9ff',
        #     'geetest_seccode': 'd5305e4eae689b3ea4715c0f68bac9ff|jordan',
        #     'geetest_challenge': '99bad51d8c559d34e9374154107ddde1jc'
        # }

if __name__ ==  '__main__':
    request = RequestJson()
    request.requestJsonKuaidi()