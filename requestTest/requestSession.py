#coding:UTF-8
#__autor__='wyxces'
import requests
# help(requests.session())

class RequestSession:
    # def requestSession(self):
    #     url = 'https://www.wanandroid.com/user/login'
    #     param = {
    #         'username': 'xin00killo',
    #         'password': 'Woaizhe1314'
    #     }
    #     #初始化session对象
    #     s = requests.session()
    #     # 通过session对象发送请求， 服务器设置在本地的cookie会保存再本地
    #     response = s.post(url= url, data= param)
    #     # 通过session继续发送post请求，自动携带上一个请求返回的cookie
    #     response2 = s.get('https://www.wanandroid.com/lg/todo/list/0')
    #     print('response2:\t',response2.text)
    #     print('response:\t',response.text)

    # def requestSessionCsdn(self):
    #     url = 'https://passport.csdn.net/v1/register/pc/login/doLogin'
    #     json_data = {"loginType":"1","pwdOrVerifyCode":"Wyxcdsn1314","userIdentification":"xin00killo","fkid":"WC39ZUyXRgdGQrzehk9W5BKI9eFs9DIwckjO0sHR8YyTMJA5J/Ctfd99zpuvdvogUDPMqBnrqV/ko8TMY3Uoikp9quubBamAInzuRIMv1unS3IxstccXNZ6IiwEEO8KLeErzxpd9YAAfBjUa79IyG9BkVzskv1gnC3osiT1o7ryTBJF//vdicor1m/6fEjwQ3jpQOtuy1hKUBmTAN4SMjSkuJ6iUZUU411nlOCeDvsuM/8slNy9spNH0BV8YoNrxx1487577677129","uaToken":"118#ZVWZzuJ26PmnCeDNEg271ZZTZsZhnZKVZHxLNfqhzHWzZgZdVfq4pZW+ZZVTVHR4Zg2ZJsqTzeBVZPx8VfqVzH2zHZZTVHW4Zhe/ZYqTzeWzIgZuXqWVze2zuZkEv2MKuRNQw7iTzHWZzZZZVoqVzeAVusCroXOGZgZauXqhzeW2ZgY2Jkq4zeOUZeZhVHC/ZZ2uZYqhzHRZZgCZXoqYZH2zZZChXHhbZZ2uZYqhzFWaZgueVoq40etPZrZuSe99ZSquXHYHozu2UF9F50Y2IZqbegcMA6BhM8K2WqPEzUKmAx+NAHiZttaYlXRZMVvBtRLOfakGqdVsMMB2vVQ9JgN0feQZuYPAPQqZZyfozsWDTy8ZXGcbYM2DxKIkdvL2bUxb6VJgcFdx8fpD+eMcOCtE2g4x8PTJUz3OCK9wuWpkXHh+pD+zmmybgIq+kf2j1l92B7BCinI0r4Dqw2q7kR6wN1cgWGrC55ZLL1GUNiyzg16O+pWaVX3Lf1bwnKzW5dXMqn9zJFyiBjS1Qozfuq1kLyISmtMfcI/CeQKId5DbPhnfWMi5MDQP2icNj9+LUQ2VUp3KL3if9FG6mOCQutXFQzn3tWYSqZbAKkoQgKVr3Ebp4DwQ0ro+3CbXKSf8Eqnm69me00csPgqm/8QInlRQRZBQ61GuOor49li/phEUjsTARqepCAxKIEB+T2ufeBOezXcP8brph3l4EDsO0YAuvAoU16J2BwxNL54cGx73RC3LUxrxI6/9JIYiQdnIKcRC70o6WpMfUWbYaR7ZKFbGHvcXCGOP6bjI1wd5zzVKbiJVrV5IAyVpx2pGhxOIsNJRRt0Q2s3Dts4s6prlaM68npqJnlXFRTcY6WTJyNmz3AcazTxYZtpC6qf11ZbmEXLZpx8rRALqSBj4iNnIy4HWwq3MPnROwgRifRmzk4aNpYqNbvF6Vu4cUQZZ0FTb1NrhbYQ9TMuztIl/sX9uqZhmYxgG307hBu974WJRNONOz/SKAGGH3CTZAk1X0AhSiowU5vqxzNrGfTBrE1dXpXksDedW2kNAvxhOigNgUGWjhg506u0MmY7RV4GxKQuSCyUEbH/h+Zayj5BZO5tcs7sHUQKtIQiRNAUmVcEEl4N2w5XHUqfGcXS9c5YAPSS/RaMCnc7/6rpJpunmNp6cNcBAF/kTq/oxH+q/dDN9eFjVI5i2Z5kg695NeCJgYblyOeXwSOBDUgw+KdIQgnRL+SOd1Wqc7KCCcqZvitZZ5iVKB6RfZX6tISiTf2tHRa22m27WnYdAgfC97rKPbnBpWHQUlLs2nyNsIlilEIjKV+GazmT7GEwUZI5rJwBwt0OFJwZyvA4W0+Hpnxjc+0fi55xsu3OlwhcnY5SSpkv+e3AVZylEZLAIy4n21oMbrugUV87kelxRNwgqiUlWqD5ot6wfZtBD4B6MRvkoq1DjqigDLC0WyJYYTVwO5nNfveWOcwW89EfV+zWaJKvsKX01AUqWfix+pg2jCbZ8c60ZBZCb2MgZxZrjYpFI1cRFI8Aa","webUmidToken":"T498822AFA86A98056927EDAE77201D1592276463C31CF1B0AF32FF6CC7"}
    #     #初始化session对象
    #     s = requests.session()
    #     # 通过session对象发送请求， 服务器设置在本地的cookie会保存再本地
    #     response = s.post(url= url, json= json_data)
    #     # 通过session继续发送post请求，自动携带上一个请求返回的cookie
    #     url2 = 'https://mp.csdn.net/mdeditor/saveArticle'
    #     param2 = {
    #         'Content-Disposition: form-data; name="type"': 'original',
    #         'Content-Disposition: form-data; name="title"': '012345',
    #         'Content-Disposition: form-data; name="tags"': '',
    #         'Content-Disposition: form-data; name="status"': '64',
    #         'Content-Disposition: form-data; name="read_need_vip"': '',
    #         'Content-Disposition: form-data; name="private"': 'true',
    #         'Content-Disposition: form-data; name="markdowncontent"': '4852134%0A',
    #         'Content-Disposition: form-data; name="id"': '90639271',
    #         'Content-Disposition: form-data; name="Description"': '5689',
    #         'Content-Disposition: form-data; name="csrf_token"': '',
    #         'Content-Disposition: form-data; name="content"': '%3Cp%3E00112311111%3C%2Fp%3E%0A%0A',
    #         'Content-Disposition: form-data; name="channel"': '37',
    #         'Content-Disposition: form-data; name="categories"': '',
    #         'Content-Disposition: form-data; name="articleedittype"': '1'
    #     }
    #     response2 = s.post(url= url2, data= param2)
    #     print('response2:\t',response2.status_code)
    #     print('response2:\t',response2.text)
    #     print('response:\t',response.text)
    def requestSessionWanandroid(self):
        url = 'https://www.wanandroid.com/user/login'
        param = {
            'username': 'xin00killo',
            'password': 'Woaizhe1314'
        }
        #初始化session对象
        s = requests.session()
        # 通过session对象发送请求， 服务器设置在本地的cookie会保存再本地
        response = s.post(url= url, data= param)
        # 通过session继续发送post请求，自动携带上一个请求返回的cookie
        url2 = 'https://www.wanandroid.com/lg/todo/add/json'
        param2 = {
            'type': '0',
            'title': '1',
            'date': '2019-05-28',
            'content': '1'
        }
        response2 = s.post(url= url2, data= param2)
        print('response2:\t',response2.text)
        print('response:\t',response.text)
if __name__ ==  '__main__':
    request = RequestSession()
    request.requestSessionWanandroid()