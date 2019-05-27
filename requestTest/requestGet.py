#coding:UTF-8
#__autor__='wyxces'

import requests

class RequestGet:
    def requestGetNoParam(self):
        print('-------requestGetNoParam-----------')
        url = 'http://10.100.13.83:8080/eagle-app/ '
        response = requests.get(url=url)
        print('url:%s,get方法，无参数：' % url)
        print('''
            contect:%s
            status_code:%s
            header:%s
            url:%s
            encoding:%s
            raw:%s
            '''
              %(response.content, response.status_code, response.headers, response.url,
                response.encoding, response.raw)
            )
    def requestGetHasParam(self):
        print('-------requestGetHasParam-----------')
        url = 'https://www.wanandroid.com/article/query'
        param = {'k': 'android'}
        response = requests.get(url=url, params=param)
        print('url:%s, get方法，有参数：%s' % (url, param))
        print('''
                    contect:%s
                    status_code:%s
                    header:%s
                    url:%s
                    encoding:%s
                    raw:%s
                    '''
                    # , 'text: % s'
              % (response.content, response.status_code, response.headers, response.url,
                 response.encoding, response.raw#, response.text
                 )
              )
    def requestGetHasTowParam(self):
        print('-------requestGetHasTowParam-----------')
        url = 'https://passport.cnblogs.com/user/LoginInfo'
        param = {'callback': 'jQuery22007184810513209827_1558966175228', '_ ': '1558966175229'}
        response = requests.get(url=url, params=param)
        print('url:%s, get方法，有参数：%s' % (url, param))
        print('''
                    contect:%s
                    status_code:%s
                    header:%s
                    url:%s
                    encoding:%s
                    raw:%s
                    '''
                  # , 'text: %s'
              % (response.content, response.status_code, response.headers, response.url,
                 response.encoding, response.raw,# response.text
                 )
              )

    def requestGetContent(self):   #例如 百度首页 用response.text 返回会有乱码  因为它时zip格式
        print('-------requestGetContent-----------')
        url = 'https://www.baidu.com/'
        response = requests.get(url=url)
        print('url:%s, get方法，无参数：' % url)
        print(#'text:', response.text,
              'concent:', response.content)

if __name__ ==  '__main__':
    request = RequestGet()
    request.requestGetNoParam()
    request.requestGetHasParam()
    request.requestGetHasTowParam()
    request.requestGetContent()
