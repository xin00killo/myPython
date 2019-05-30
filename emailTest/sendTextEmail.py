# coding:UTF-8
# __autor__ = 'wyxces'

import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_port =25
# 第三方 smtp服务配置
mail_host = 'smtp.163.com'
mail_user = 'xin00killo@163.com'
mail_pass = 'xin00killo'
# 邮件属性配置
sender = 'xin00killo@163.com'
receivers = ['xin01killo@163.com', 'xin02killo@163.com']
# ['xin00killo@163.com', 'xin01killo@163.com']

#三个参数， 第一个为文本内容，第二个plain设置文本格式，第3个urf-8设置编码
msg = MIMEText('''
                wyxces python 发送邮件内容在这里:
                001
                002
                003
                004
            ''', 'plain', 'utf-8')
# msg['From'] = Header(' xin01killo')
# msg['To'] = Header('xin02killo')
msg['From'] = "xin00killo<xin00killo@163.com>"
msg['To'] = ','.join(["xin01killo<xin01killo@163.com>", "xin02killo<xin02killo@163.com>"])
subject = 'wyxces python email0019'
msg['Subject'] = Header(subject, 'utf-8')


try:
    smtpObject = smtplib.SMTP()
    smtpObject.connect(host=mail_host, port=25)
    smtpObject.login(user=mail_user, password=mail_pass)
    smtpObject.sendmail(sender, receivers, msg.as_string())
    print('发送邮件成功')
except smtplib.SMTPException as smtpMsg :
    print('邮件发送失败，', smtpMsg)
