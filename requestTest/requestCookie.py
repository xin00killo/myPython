#coding:UTF-8
#__autor__='wyxces'

import requests

class RequestCookie:
    def requestCooke_01_wanandroid(self):
        print('-------requestCooke_01_wanandroid-----------'
              '\n-------1、通过r.cookies手动获取上一请求返回的cookie来设置下次请求的cookie')
        url = 'https://www.wanandroid.com/user/login'
        param = {
            'username': 'xin00killo',
            'password': 'Woaizhe1314'
        }
        r = requests.post(url= url, data= param)
        print('''
                url = %s
                cookies:%s
                headers:%s
            '''
            %(url, r.cookies, r.headers)
              )
        #获取上次请求放回的response中的cookies，传递给下次请求
        cookie = r.cookies
        print('cookie = r.cookies', cookie)
        #携带cookie发送请求
        url2 = 'https://www.wanandroid.com/lg/todo/list/0'
        r2 = requests.get(url= url2, cookies= cookie)
        print('''
                url2 = %s
                cookies:%s
                headers:%s
                status:%s
                text:%s
            '''
              %(url2, r2.cookies, r2.headers, r2.status_code, r2.text))


    def requestCooke_02_wanandroid(self):
        print('-------requestCooke_02_wanandroid-----------'
              '\n-------2、通过rquests.session自动设置cookie，来完成访问')
        url = 'https://www.wanandroid.com/user/login'
        param = {
            'username': 'xin00killo',
            'password': 'Woaizhe1314'
        }
        # 初始化session对象
        s = requests.session()
        # 通过session对象，发送请求
        r = s.post(url=url, data=param)
        print('''
                       url = %s
                       cookies:%s
                       headers:%s
                   '''
              % (url, r.cookies, r.headers)
              )
        #通过session继续发送get请求，自动携带上一个请求返回的cookie
        url2 = 'https://www.wanandroid.com/lg/todo/add/json'
        param2 = {
            'type': '0',
            'title': 'title：requestCooke_02_wanandroid',
            'date': '2019-05-28',
            'content': 'content：requestCooke_02_wanandroid'
        }
        r2 = s.post(url= url2, data= param2)
        print('''
                url2 = %s
                cookies:%s
                headers:%s
                status:%s
                connect:%s
            '''
              %(url2, r2.cookies, r2.headers, r2.status_code, r2.content))

    def requestCooke_03_wanandroid(self):
        print('-------requestCooke_03_wanandroid-----------'
              '\n-------3、通过定制cookie，单独设置cookie来访问目标网址')
        url = 'https://www.wanandroid.com/user/login'
        param = {
            'username': 'xin00killo',
            'password': 'Woaizhe1314'
        }
        r = requests.post(url=url, data=param)
        print('''
                       url = %s
                       cookies:%s
                       headers:%s
                   '''
              % (url, r.cookies, r.headers)
              )

        #获取上次请求放回的response中的cookie，通过字典的形式引用cookie返回的JSESSIONID，放入cookie中
        cookie = {'JSESSIONID': r.cookies['JSESSIONID']}
        url2 = 'https://www.wanandroid.com/lg/todo/add/json'
        param2 = {
            'type': '0',
            'title': 'title：requestCooke_03_wanandroid',
            'date': '2019-05-28',
            'content': 'content：requestCooke_03_wanandroid'
        }
        r2 = requests.post(url= url2, data= param2, cookies=cookie)
        print('''
                url2 = %s
                cookies:%s
                headers:%s
                status:%s
                connect:%s
            '''
              % (url2, r2.cookies, r2.headers, r2.status_code, r2.content))

    def requestCooke_04_wanandroid(self):
        print('-------requestCooke_04_wanandroid-----------'
              '\n-------4、通过定制cookie，放入header来访问目标网址')
        url = 'https://www.wanandroid.com/user/login'
        param = {
            'username': 'xin00killo',
            'password': 'Woaizhe1314'
        }
        r = requests.post(url=url, data=param)
        print('''
                       url = %s
                       cookies:%s
                       headers:%s
                   '''
              % (url, r.cookies, r.headers)
              )

        #获取上次请求放回的response中的cookie，通过字典的形式引用cookie返回的JSESSIONID，放入下次请求的header中
        header = {'cookie':'JSESSIONID='+ r.cookies['JSESSIONID']}
        url2 = 'https://www.wanandroid.com/lg/todo/add/json'
        param2 = {
            'type': '0',
            'title': 'title：requestCooke_04_wanandroid',
            'date': '2019-05-28',
            'content': 'content：通过定制cookie，放入header来访问目标网址'
        }
        r2 = requests.post(url= url2, data= param2, headers= header)
        print('''
                url2 = %s
                cookies:%s
                headers:%s
                status:%s
                connect:%s
            '''
              % (url2, r2.cookies, r2.headers, r2.status_code, r2.content))
        #str.find 方法返回 -1:表示未找到， 非-1:表示找到
        result = r2.text.find('已完成清单')
        print('已完成清单是否找到：',result)

if __name__ ==  '__main__':
    request = RequestCookie()
    # request.requestCooke_01_wanandroid()
    # request.requestCooke_02_wanandroid()
    # request.requestCooke_03_wanandroid()
    request.requestCooke_04_wanandroid()