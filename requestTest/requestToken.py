# coding:utf-8

import requests
import re
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()
import hashlib

class requestToken:
    def getTokenCode(self, session):
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
        tokenCode = {}
        try:
            t = soup.find_all('script')[1].get_text()
            # print('--t--',t)
            tokenCode['window.X_Anti_Forge_Token'] = re.findall(r"Token = '(.+?)'", t)[0]
            tokenCode['window.X_Anti_Forge_Code'] = re.findall(r"Code = '(.+?)'", t)[0]
        except:
            print('获取token失败')
            tokenCode['window.X_Anti_Forge_Token'] = ""
            tokenCode['window.X_Anti_Forge_Code'] = ""
        # print('tokenCode:', tokenCode)
        return tokenCode

    def encryptPwd(self, passwd):
        #对密码进行了md5双重加密
        passwd = hashlib


if __name__ ==  '__main__':
    requestGet = requestToken()
    session = requests.session()
    print(requestGet.getTokenCode(session))