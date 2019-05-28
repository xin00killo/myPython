#coding:UTF-8
#__autor__='wyxces'

#coding:UTF-8
#__autor__='wyxces'

import requests, json

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

class RequestPostData:
    def requestPostDataCnblogs(self):
        url = 'https://account.cnblogs.com/Account/SignIn?returnurl=https%3A%2F%2Fwww.cnblogs.com%2F'
        print('url:', url)
        data = {
            'LoginName': 'Lc198Box3%2FTd9ZcclG9cYgX3Wj2vxlOMkEQAb%2FzhXGUgedWTu4U%2F4OuayREqLHlghXGjRzSW6i7tm076drbIggTxIbHWKN1nZMR93%2FDgkqUenYcqH1IBLmpH59QUK28DrhB9aJaS9Rz3382dcV15LN6%2Bf1Tac9CYgwaGxZ1CmQE%3D',
            'Password': 'cMZ2ArMHjCZ%2FezDzX2EeteGtjJD6Q9QALWK7gGBEOWPUT4w2hU%2Fn4EBNaB%2FE3wCyJ6eKXoMpUy4WVnEOw9ZiLVQjmtS6fnagsUoCTmfEIuYk%2FDC2lDVq1XhiFJDVDwiZzp4Im0Njz%2F3%2BHnEXTtW%2Bk%2Be%2BPS5KyGuwNUD1YTr7VdI%3D',
            'PublicKey': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCp0wHYbg%2FNOPO3nzMD3dndwS0MccuMeXCHgVlGOoYyFwLdS24Im2e7YyhB0wrUsyYf0%2FnhzCzBK8ZC9eCWqd0aHbdgOQT6CuFQBMjbyGYvlVYU2ZP7kG9Ft6YV6oc9ambuO7nPZh%2BbvXH0zDKfi02prknrScAKC0XhadTHT3Al0QIDAQAB',
            'EnableCaptcha': 'true',
            '__RequestVerificationToken': 'CfDJ8D8Q4oM3DPZMgpKI1MnYlrnleaXU1rFAZHB_fIIUBuEw3g0KtEvcbbR6tv0VG5p1VTovWVCoWry730jwutBMisZIb-Hr7gwYeKcQfCU7FRwM7EZ0fSky_2mHOL6ahlUs0ADrgYxpOrbQdoJS8QUSAxM',
            'IsRemember': 'false',
            'isEncrypted': 'true',
            'geetest_challenge': '2e52d0bbfd92da316dec062b5c77a75db3',
            'geetest_validate': '618f5fd6dea46863a3d269d8262e06bb',
            'geetest_seccode': '618f5fd6dea46863a3d269d8262e06bb%7Cjordan'
        }
        response = requests.post(url=url, data=data)
        print('\tstatus_code', response.status_code,
              '\n\ttext', response.text
              )

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


class RequestSession:
    def requestSessionWanandroid(self):
        print('-------requestSessionWanandroid-----------')
        url = 'https://www.wanandroid.com/user/login'
        param = {
            'username': 'xin00killo',
            'password': 'Woaizhe1314'
        }
        # 初始化session对象
        s = requests.session()
        # 通过session对象发送请求， 服务器设置在本地的cookie会保存再本地
        response = s.post(url=url, data=param)
        # 通过session继续发送post请求，自动携带上一个请求返回的cookie
        url2 = 'https://www.wanandroid.com/lg/todo/add/json'
        param2 = {
            'type': '0',
            'title': '1',
            'date': '2019-05-28',
            'content': '1'
        }
        response2 = s.post(url=url2, data=param2)
        print('response2:\t', response2.text)
        print('response:\t', response.text)

class RequestJson:
    def requestJsonKuaidi(self):
        print('-------requestJsonKuaidi-----------')
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
    requestGet = RequestGet()
    requestGet.requestGetNoParam()
    requestGet.requestGetHasParam()
    requestGet.requestGetHasTowParam()
    requestGet.requestGetContent()

    requestPostData = RequestPostData()
    requestPostData.requestPostDataCnblogs()

    requestPostJson = RequestPostJson()
    requestPostJson.requestPostJsonDumps()
    requestPostJson.requestPostJsonJson()

    requestSession = RequestSession()
    requestSession.requestSessionWanandroid()

    requestJson = RequestJson()
    requestJson.requestJsonKuaidi()

    requestCookie = RequestCookie()
    requestCookie.requestCooke_01_wanandroid()
    requestCookie.requestCooke_02_wanandroid()
    requestCookie.requestCooke_03_wanandroid()
    requestCookie.requestCooke_04_wanandroid()