#coding:UTF-8
#__autor__='wyxces'

import requests

class RequestPostData:
    def requestPostDataCnblogs(self):
        url = 'https://account.cnblogs.com/Account/SignIn'
        print('url:', url)
        param = {'returnurl': 'https%3A%2F%2Fwww.cnblogs.com%2F'}
        data = {
            'LoginName': 'Lc198Box3%2FTd9ZcclG9cYgX3Wj2vxlOMkEQAb%2FzhXGUgedWTu4U%2F4OuayREqLHlghXGjRzSW6i7tm076drbIggTxIbHWKN1nZMR93%2FDgkqUenYcqH1IBLmpH59QUK28DrhB9aJaS9Rz3382dcV15LN6%2Bf1Tac9CYgwaGxZ1CmQE%3D',
            'Password': 'cMZ2ArMHjCZ%2FezDzX2EeteGtjJD6Q9QALWK7gGBEOWPUT4w2hU%2Fn4EBNaB%2FE3wCyJ6eKXoMpUy4WVnEOw9ZiLVQjmtS6fnagsUoCTmfEIuYk%2FDC2lDVq1XhiFJDVDwiZzp4Im0Njz%2F3%2BHnEXTtW%2Bk%2Be%2BPS5KyGuwNUD1YTr7VdI%3D',
            'PublicKey': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCp0wHYbg%2FNOPO3nzMD3dndwS0MccuMeXCHgVlGOoYyFwLdS24Im2e7YyhB0wrUsyYf0%2FnhzCzBK8ZC9eCWqd0aHbdgOQT6CuFQBMjbyGYvlVYU2ZP7kG9Ft6YV6oc9ambuO7nPZh%2BbvXH0zDKfi02prknrScAKC0XhadTHT3Al0QIDAQAB',
            'EnableCaptcha': 'true',
            '__RequestVerificationToken': 'CfDJ8D8Q4oM3DPZMgpKI1MnYlrnleaXU1rFAZHB_fIIUBuEw3g0KtEvcbbR6tv0VG5p1VTovWVCoWry730jwutBMisZIb-Hr7gwYeKcQfCU7FRwM7EZ0fSky_2mHOL6ahlUs0ADrgYxpOrbQdoJS8QUSAxM',
            'IsRemember': 'false',
            'EnableCaptcha': 'false',
            'isEncrypted': 'true',
            'geetest_challenge': '2e52d0bbfd92da316dec062b5c77a75db3',
            'geetest_validate': '618f5fd6dea46863a3d269d8262e06bb',
            'geetest_seccode': '618f5fd6dea46863a3d269d8262e06bb%7Cjordan'
        }
        response = requests.post(url=url, data=data, params=param)
        print('\tstatus_code', response.status_code,
              '\n\ttext', response.text
              )
    def requestPostDataGeetest(self):
        url = 'https://api.geetest.com/gt_judgement'
        print('url:', url)
        param = {'pt': '0', 'gt': '66442f2f720bfc86799932d8ad2eb6c7'}
        data = 'nLYvtlnNYdUU68IXi84sdryl9ucQ2skF5u8LBLKXarWE41fPrzcL7yxmf2fYN2XDG1CyhqjVaXyi2Q)3oBs537a1dNTMv4w)U5b23FFwHcWMk(3gtb8VHP7U0ltLOistf5IoI5Bt11GMavQSlQJ(ga)AsFh0wTLAC9yNwbdBfZExS0TT)Ojw010QuOFPQg2sj2jvTEER1LRMLHmQKR0KjWN)4Cq2o2WUzhwPy7sFFxJuCxUO)5377hbgo5tdjTOFHwgkUqZrY1lkmsPmexujXXIgpN9p2aa5OQ)iMRZ(p0zfuAnBYAEBOy6H6vSopUiWGeNg(IO(ppE7X0b6Zpul)GqoNs3nuVCdlamTyui5qKhr8fyFSgzxiYWamJ5xR8PbvM9XQLEPZnxqvL(2P3nuRwa4S8qTzbMTwN3fw)KvEXUC2iatqz4G6ExOcfcUbQtRp7I1fEgjNb7Y8DEAZwmqyBG0qUVc3moKM8KZrWLZxR14Wp8AaG3WzJ)s4z9ouViog8nAt1PI6xlPHWKazr7bH1mfpKYmz8z2k)TKYeQtG9XAjjWtab(dr5AsPjQk1njJmgAI(48Bh7pLzZwJIW93YAtExbuCHGauxyEU28ZrKrqTjlgqu7KeurQU5hu(DhlIdMkmRqI(xguC8GjkYAlXF7aOjSvDwkxLUrLEE44CBe2gGNEFn6uax6HhvcUHIRMtIq0BB5Va4i)hnTK)WzcH2jetHMn4KVgFykF8NTKpWIkt(qIhiW)V1DNlfbmQi0ZmpUbLyOnLX42cjxwFh5Rnxrq(4WsPVm(Y8Oz0WtPaniTrAE6hFrdXS8PKyyefa49QcTFDJr9nrCgv5bu1dg6m5jVvypdt7mKGRpy3DILQ)TZ0LX6OHBwl)4375P0X9QEXf6Dl4r9)0gNi(xSfT0FYLNJVzMfk)cNulnhOzjpDisiUu5oZHtAK0ue9BiFa40lwSXDmAHxm5DcCmkaK1eINzFTplJt9Gk5KcDxqJPCYhNX1gvXmLBpKRcgqXZmIWRU6nYmkF76WLImaEhN)HK4RYPiGCvUt3(23sAmuJoFyHEsmTLbq13KRWY0tUbKhJjcPlOJUHduT1aSiWalhY0GTfhTiHfAu09zqENSHxVMAxtzi8FVSSZfPP82eIOyphvu(gukLDRaARVVAB4QFfgAxPSDWjRAT28IkMd1SiPug(fuJ9M61l2PzMiNxfZ6TXCtgUvmkOHgIybDYdPM6PB4ObXbV2wQf0q939Mkm8eVNsMvNPRZ0b1oJo0AnCz1IsxFn4JfCpB8M328wtH)7ve1jOBB4KulYQlXJuI3HUCJoUU5I0V)xAZhRI)nX0cepkfkCMwOjKmIihoLXA3y2Z8p3r04s9NZc8ngBkdacFpqYtnR19EmDeMoKgay8PGQ)(zZf1hHhWXuZWXTXdyR)KDvRdlx9wjG2FhV95QAH3aG85Dxufapym)b6kWJzKFw(qmsSpvUwUDhVQN2lfeUjR27eb2JZ0WP1GkQfG4LZ1CJYrBcfTx3zLD))kwiq3ScaVbT)B1GVfXqEP68zeLs9J)xwU7NgsI(QKtNw7WpymPl(g(FmDmxzrAMarwdqdoG2)KJRX5Qjz)ke8VnU8A09PVsdEwWKtkXjMUbvB)7Z3OFFOA(2EoKwthpb(mMyiUghjLD9(JXfqGm2k4RVF8vATKIo7YGKgadiI5vwzs0EOdpChJVk5E7c3MMCiuUHm9axWXP0i0)PmW(ZxoiT0ZJvnyCCn60nwyjKHpp5nXnN2SKZS8WBliyhdc8RUqVRnZeh0pH27jiPUGXYkRiAuoKDzl8S6l3NWm6xPPQw1MbldzTqmMTUsOuoR5CBzlU)TJl2gCSRgE1j(ChpXGSUfUvuTwaGBFfKWyQWsWdSbcC2tSEF2WP4lSdgEntDioWtRFeGUNg8tlnswrkfS6JhgE7BgfC36H(X1fytovT3vuTwilxGIt2xWuD9iY1Qxf9CtgSvo7vJTWmYneAQEyOUyqwcF5e6un(GCrMa7sizPHqf)gPseC2CeCQH9anwH7ZHiLiMRznWM(mH1CJEt52ez)IeiVTaDFpy1oYhURRwGoxMU2MkqIkw4LBR59MuKpBUdS6kZWcr(GwZ7VBLE3GAsX8ndtwoLAmeifdRQIonF7L1qozAKBU7lyJM2oqYXs(7gLJZyIWmTXVskE8iAIXp)yRtajPfnTintzNxGHEKCyVZQrr0XBEvt3UtksAv9(1V2N8EBn7Hkb8VKw5u6BdFnc0dMQqgum(zQaTb(URg4(O9EmTXcQSpLTm4IRX(Pm)44ZYezGD(8BZoukh7Mhko6a1LizgNMdmizc)F9YBHLXXdwec1wK8OAnQcZt7rbVfIl6Vd3HqoQdcId8B)NiAT4YWhJM39jEYbgBVzBhunEFV8DjTVSqudgf009qrFN(xrIo(EP5Wo6fYmTd7X4NMjElvOOm(2SV00ftg7d7(oUwkCHcEvQieQSZe(lmxeuIS0UMLAJ0nlyfFvrf0wr2oTKek1wu0)p17viMriD8ONEOqY9bqsKZBhtiGxgzN3pTYlj3vYDMSbylh02H5iFn)efqRTD8s8amfw645BqAGI65uTRAeGLTTq6tAZex(Cfo4r21MQxKgkREGGhoky)3cKWA97jirImA..4f0ae6c11327e4367bff580c5b909a03039cf44f566fad8680886dd52987bd4956933bdd2376e53c282edd8a5b79e38d2d078bc9a1eb186462d24ed2bc4cba3b2eda457b80a6dd8b1394e159b1a2d72d2f500a2b2703e372ade0e97fd741d75d6f401801e1022fd8772a463a15ce646ca0d00efe04500dfddd33f46e037bdb20'
        response = requests.post(url=url, data=data, params=param)
        print('\tstatus_code', response.status_code,
              '\n\ttext', response.text
              )

if __name__ ==  '__main__':
    request = RequestPostData()
    request.requestPostDataGeetest()