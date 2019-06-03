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
    def getChallenge(self):
        url = 'https://api.geetest.com/gt_judgement'
        print('url:', url)
        param = {'pt': '0', 'gt': '66442f2f720bfc86799932d8ad2eb6c7'}
        data = 'nLYvtlnNYdUU68IXi84sdryl9ucQ2skF5u8LBLKXarWE41fPrzcL7yxmf2fYN2XDG1CyhqjVaXyi2Q)3oBs537a1dNTMv4w)U5b23FFwHcWMk(3gtb8VHP7U0ltLOistf5IoI5Bt11GMavQSlQJ(ga)AsFh0wTLAC9yNwbdBfZExS0TT)Ojw010QuOFPQg2sj2jvTEER1LRMLHmQKR0KjWN)4Cq2o2WUzhwPy7sFFxJuCxUO)5377hbgo5tdjTOFHwgkUqZrY1lkmsPmexujXXIgpN9p2aa5OQ)iMRZ(p0zfuAnBYAEBOy6H6vSopUiWGeNg(IO(ppE7X0b6Zpul)GqoNs3nuVCdlamTyui5qKhr8fyFSgzxiYWamJ5xR8PbvM9XQLEPZnxqvL(2P3nuRwa4S8qTzbMTwN3fw)KvEXUC2iatqz4G6ExOcfcUbQtRp7I1fEgjNb7Y8DEAZwmqyBG0qUVc3moKM8KZrWLZxR14Wp8AaG3WzJ)s4z9ouViog8nAt1PI6xlPHWKazr7bH1mfpKYmz8z2k)TKYeQtG9XAjjWtab(dr5AsPjQk1njJmgAI(48Bh7pLzZwJIW93YAtExbuCHGauxyEU28ZrKrqTjlgqu7KeurQU5hu(DhlIdMkmRqI(xguC8GjkYAlXF7aOjSvDwkxLUrLEE44CBe2gGNEFn6uax6HhvcUHIRMtIq0BB5Va4i)hnTK)WzcH2jetHMn4KVgFykF8NTKpWIkt(qIhiW)V1DNlfbmQi0ZmpUbLyOnLX42cjxwFh5Rnxrq(4WsPVm(Y8Oz0WtPaniTrAE6hFrdXS8PKyyefa49QcTFDJr9nrCgv5bu1dg6m5jVvypdt7mKGRpy3DILQ)TZ0LX6OHBwl)4375P0X9QEXf6Dl4r9)0gNi(xSfT0FYLNJVzMfk)cNulnhOzjpDisiUu5oZHtAK0ue9BiFa40lwSXDmAHxm5DcCmkaK1eINzFTplJt9Gk5KcDxqJPCYhNX1gvXmLBpKRcgqXZmIWRU6nYmkF76WLImaEhN)HK4RYPiGCvUt3(23sAmuJoFyHEsmTLbq13KRWY0tUbKhJjcPlOJUHduT1aSiWalhY0GTfhTiHfAu09zqENSHxVMAxtzi8FVSSZfPP82eIOyphvu(gukLDRaARVVAB4QFfgAxPSDWjRAT28IkMd1SiPug(fuJ9M61l2PzMiNxfZ6TXCtgUvmkOHgIybDYdPM6PB4ObXbV2wQf0q939Mkm8eVNsMvNPRZ0b1oJo0AnCz1IsxFn4JfCpB8M328wtH)7ve1jOBB4KulYQlXJuI3HUCJoUU5I0V)xAZhRI)nX0cepkfkCMwOjKmIihoLXA3y2Z8p3r04s9NZc8ngBkdacFpqYtnR19EmDeMoKgay8PGQ)(zZf1hHhWXuZWXTXdyR)KDvRdlx9wjG2FhV95QAH3aG85Dxufapym)b6kWJzKFw(qmsSpvUwUDhVQN2lfeUjR27eb2JZ0WP1GkQfG4LZ1CJYrBcfTx3zLD))kwiq3ScaVbT)B1GVfXqEP68zeLs9J)xwU7NgsI(QKtNw7WpymPl(g(FmDmxzrAMarwdqdoG2)KJRX5Qjz)ke8VnU8A09PVsdEwWKtkXjMUbvB)7Z3OFFOA(2EoKwthpb(mMyiUghjLD9(JXfqGm2k4RVF8vATKIo7YGKgadiI5vwzs0EOdpChJVk5E7c3MMCiuUHm9axWXP0i0)PmW(ZxoiT0ZJvnyCCn60nwyjKHpp5nXnN2SKZS8WBliyhdc8RUqVRnZeh0pH27jiPUGXYkRiAuoKDzl8S6l3NWm6xPPQw1MbldzTqmMTUsOuoR5CBzlU)TJl2gCSRgE1j(ChpXGSUfUvuTwaGBFfKWyQWsWdSbcC2tSEF2WP4lSdgEntDioWtRFeGUNg8tlnswrkfS6JhgE7BgfC36H(X1fytovT3vuTwilxGIt2xWuD9iY1Qxf9CtgSvo7vJTWmYneAQEyOUyqwcF5e6un(GCrMa7sizPHqf)gPseC2CeCQH9anwH7ZHiLiMRznWM(mH1CJEt52ez)IeiVTaDFpy1oYhURRwGoxMU2MkqIkw4LBR59MuKpBUdS6kZWcr(GwZ7VBLE3GAsX8ndtwoLAmeifdRQIonF7L1qozAKBU7lyJM2oqYXs(7gLJZyIWmTXVskE8iAIXp)yRtajPfnTintzNxGHEKCyVZQrr0XBEvt3UtksAv9(1V2N8EBn7Hkb8VKw5u6BdFnc0dMQqgum(zQaTb(URg4(O9EmTXcQSpLTm4IRX(Pm)44ZYezGD(8BZoukh7Mhko6a1LizgNMdmizc)F9YBHLXXdwec1wK8OAnQcZt7rbVfIl6Vd3HqoQdcId8B)NiAT4YWhJM39jEYbgBVzBhunEFV8DjTVSqudgf009qrFN(xrIo(EP5Wo6fYmTd7X4NMjElvOOm(2SV00ftg7d7(oUwkCHcEvQieQSZe(lmxeuIS0UMLAJ0nlyfFvrf0wr2oTKek1wu0)p17viMriD8ONEOqY9bqsKZBhtiGxgzN3pTYlj3vYDMSbylh02H5iFn)efqRTD8s8amfw645BqAGI65uTRAeGLTTq6tAZex(Cfo4r21MQxKgkREGGhoky)3cKWA97jirImA..4f0ae6c11327e4367bff580c5b909a03039cf44f566fad8680886dd52987bd4956933bdd2376e53c282edd8a5b79e38d2d078bc9a1eb186462d24ed2bc4cba3b2eda457b80a6dd8b1394e159b1a2d72d2f500a2b2703e372ade0e97fd741d75d6f401801e1022fd8772a463a15ce646ca0d00efe04500dfddd33f46e037bdb20'
        response = requests.post(url=url, data=data, params=param)
        challenge = ''
        try:
            challenge = response.json()['challenge']
        except Exception as msg:
            print('获取challenge失败', msg)
        print('challenge:', challenge)
        return challenge
    def login(self, user, password):
        session = requests.session()
        tokenData = self.getTokenData(session)
        challenge = self.getChallenge()
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
            'challenge': challenge
        }
        response = session.post(url=url, data=param, headers=header, verify=False)
        print(response.status_code)
        try:
            print('登录信息：', response.text)
            # return response.json()
        except BaseException as msg:
            print('登录信息异常',msg)
            # return None


if __name__ ==  '__main__':
    requestToken = requestToken()
    # session = requests.session()
    # print(requestToken.getTokenData(session))
    # 密码加密是不变的 password=5bb004e41f4feee4aaa4bc762d8f6eae
    user = 13041021995
    password = '5bb004e41f4feee4aaa4bc762d8f6eae'
    requestToken.login(user, password)
