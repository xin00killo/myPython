#coding:UTF-8
#__autor__='wyxces'

import requests

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
            'EnableCaptcha': 'false',
            'isEncrypted': 'true',
            'geetest_challenge': '2e52d0bbfd92da316dec062b5c77a75db3',
            'geetest_validate': '618f5fd6dea46863a3d269d8262e06bb',
            'geetest_seccode': '618f5fd6dea46863a3d269d8262e06bb%7Cjordan'
        }
        response = requests.post(url=url, data=data)
        print('\tstatus_code', response.status_code,
              '\n\ttext', response.text
              )


if __name__ ==  '__main__':
    request = RequestPostData()
    request.requestPostDataCnblogs()