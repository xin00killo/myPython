# coding:UTF-8
# __autor__ = 'wyxces'

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_port = 25
mail_host = 'smtp.163.com'
mail_user = 'xin00killo@163.com'
mail_pass = '9999'

sender = 'xin00killo@163.com'
receivers = ['xin01killo@163.com', 'xin02killo@163.com']

# Python发送HTML格式的邮件与发送纯文本消息的邮件不同之处就是
# 将MIMEText中_subtype设置为html。具体代码如下：

content = '''
    mail_msg 这里是邮件正文
    <p> Python 邮件发送，html</p>
    <p><a href='http://www.baidu.com'>这是一个会跳转到百度首页的连接</a></p>
'''

message = MIMEText(content, 'html', 'utf-8')
message['From'] = 'xin00killo<xin00killo@163.com>'
message['To'] = ','.join(receivers)


title = 'wyx python html'
message['Subject'] = Header(title, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(host=mail_host, port=mail_port)
    smtpObj.login(user=mail_user, password=mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as smtpMsg:
    print('邮件发送失败：', smtpMsg)

