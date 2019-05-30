#coding:UTF-8
#__autor__='wyxces'

import smtplib
import os
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email.header import Header

mail_port = 25
mail_host = 'smtp.163.com'
mail_user = 'xin01killo@163.com'
mail_pass = '9999'
sender = mail_user
receivers = ['xin00killo@163.com', 'xin02killo@163.com']


# 创建根消息并填写“发件人”、“收件人”和“主题”标题
msgObj = MIMEMultipart('related') #设置邮件为多文本格式
msgObj['From'] = mail_user
msgObj['To'] = ','.join(receivers)
msgObj['Cc'] = mail_user  # 这个是抄送的意思不？
msgObj['Subject'] = 'wyx python image'

# 将消息正文的纯文本和HTML版本封装在“可选”部分中，以便消息代理可以决定要显示哪个版本。
msgAlternative = MIMEMultipart('alternative')
msgObj.attach(msgAlternative)

# 指定图片
dirPath = os.path.dirname(__file__) + '/attachAndImage/'
imageName = 'image.jpg'
imagePath = dirPath + imageName
image = open(imagePath, 'rb')
msgImage = MIMEImage(image.read())
image.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgObj.attach(msgImage)

# 邮件正文
content = '''
            python wyxces image 
            <a herf='www.baidu.com'> 这里是一个会调转到百度首页的连接</a>
            图片演示：\n
            <img src='cid:image1'>
        '''
msgAlternative.attach(MIMEText(content, 'html', 'utf-8'))

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(host=mail_host, port=mail_port)
    smtpObj.login(user=mail_user, password=mail_pass)
    smtpObj.sendmail(sender, receivers, msgObj.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as smtpMsg:
    print('邮件发送失败：', smtpMsg)