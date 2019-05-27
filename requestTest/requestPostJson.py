#coding:UTF-8
#__autor__='wyxces'

import requests,json

class RequestPostJson:
    def requestPostJsonDumps(self):
        print('-------requestPostJsonDumps-----------')
        url = 'http://httpbin.org/post'
        payload = {'qq群名':'selenium+jmter+loanrunner', 'qq群号':'106014970'}
        payload = json.dumps(payload)
        response = requests.post(url=url, data=payload)
        # print(response.text)
        print(response.json())
    def requestPostJsonJson(self):
        print('-------requestPostJsonJson-----------')
        url = 'http://httpbin.org/post'
        payload = {'qq群名':'selenium+jmter+loanrunner', 'qq群号':'106014970'}
        response = requests.post(url=url, json=payload)
        # print(response.text)
        print(response.json())


if __name__ ==  '__main__':
    request = RequestPostJson()
    request.requestPostJsonDumps()
    request.requestPostJsonJson()