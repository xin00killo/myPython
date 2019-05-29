# coding:utf-8

import requests
import re
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()
import hashlib

class requestToken:
    def getTokenData(self, session):
        url = 'https://passport.lagou.com/login/login.html'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        # 更新session 的headers
        session.headers.update(header)
        response = session.get(url, verify=False)
        # print(response.content)
        soup = BeautifulSoup(response.content, "html.parser", from_encoding='utf-8')
        # print('soup',soup)
        tokenData = {}
        try:
            t = soup.find_all('script')[1].get_text()
            # print('--t--',t)
            tokenData['Token'] = re.findall(r"Token = '(.+?)'", t)[0]
            tokenData['Code'] = re.findall(r"Code = '(.+?)'", t)[0]
        except:
            print('获取token失败')
            tokenData['Token'] = ""
            tokenData['Code'] = ""
        # print('tokenCode:', tokenCode)
        return tokenData
    def login(self, user, password):
        session = requests.session()
        tokenData = self.getTokenData(session)
        # print(tokenData)
        url = 'https://passport.lagou.com/login/login.html'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Anit-Forge-Token': tokenData['Token'],
            'X-Anit-Forge-Code': tokenData['Code'],
            'Referer': 'https://passport.lagou.com/login/login.html'
        }
        param = {
            'isValidate': 'true',
            'username': user,
            'password': password,
            'challenge': '41b7cd452d780b4ba04d8b6eb7a1effb'
        }
        response = session.post(url=url, data=param, headers=header, verify=False)
        print(response.status_code)
        try:
            print('登录信息：', response.text)
            return response.json()
        except BaseException as msg:
            print('登录信息异常',msg)
            return None


if __name__ ==  '__main__':
    requestToken = requestToken()
    # session = requests.session()
    # print(requestToken.getTokenData(session))
    # 密码加密是不变的 password=5bb004e41f4feee4aaa4bc762d8f6eae
    user = 13041021995
    password = '5bb004e41f4feee4aaa4bc762d8f6eae'
    requestToken.login(user, password)
