#coding:UTF-8
#__autor__='wyxces'

import smtplib,os
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_port = 25
mail_host = 'smtp.163.com'
mail_user = 'xin01killo@163.com'
mail_pass = '9999'

sender = mail_user
receivers = ['xin00killo@163.com', 'xin02killo@163.com']
# 创建一个带附件的实例
msgObj = MIMEMultipart()
msgObj['From'] = sender
msgObj['To'] = ','.join(receivers)
msgObj['Cc'] = mail_user  # 这个是抄送的意思不？
subject = 'wyx python sendAttachEmail 5'
msgObj['Subject'] = Header(subject, 'utf-8')

#邮件正文内容
content = '''
            wyx python sendAttachEmail content
        '''
# msgObj = MIMEText(content, 'html', 'utf-8')  普通 html 的 长这个样子的
msgObj.attach(MIMEText(content, 'plain', 'utf-8'))

dirPath = os.path.dirname(__file__) + '/attachAndImage/'
#构造附件1  使用菜鸟教程上的方法
attachTxtName = 'attach001.txt'
attachTxtPath = dirPath + attachTxtName
attachTxt = MIMEText(open(attachTxtPath, 'rb').read(), 'base64', 'utf-8')
attachTxt['Content-Type'] = 'application/octet-stream'
#这里的filename可以任意写，写什么名字，邮件中显示什么名字
attachTxt['Content-Disposition'] = 'attachment; filename=' + attachTxtName
msgObj.attach(attachTxt)

#构造附件2 使用第二种方法试试
attachJsonName = 'attach002.json'
attachJsonPath = dirPath + attachJsonName
attachJson = MIMEApplication(open(attachJsonPath,'rb').read())
attachJson.add_header('Content-Disposition', 'attachment', filename=attachJsonName)
msgObj.attach(attachJson)


#构造附件3 使用廖雪峰官网上的方法写
attachImageName = 'pythonAttach.png'
attachImagePath = dirPath + attachImageName
with open(attachJsonPath,'rb') as f:
    attachImage = MIMEBase('image','png',filename=attachImageName)
    attachImage.add_header('Content-Disposition', 'attachment', filename=attachImageName)
    attachImage.add_header('Content-ID','<0>')
    attachImage.add_header('X-Attachement-Id', '0')
    #把附件的内容读进来
    attachImage.set_payload(f.read())
    encoders.encode_base64(attachImage)
    msgObj.attach(attachImage)

#构造附件4 发送图片附件
ctype = 'application/octet-stream'
maintype, subtype = ctype.split('/', 1)
attachImage1Name = 'image.jpg'
attachImage1Path = dirPath + attachJsonName
attachImage1 = MIMEImage(open(attachJsonPath,'rb').read(), _subtype=subtype)
attachImage1.add_header('Content-Disposition', 'attachment', filename='attachImage1Name.png')
msgObj.attach(attachImage1)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(host=mail_host, port=mail_port)
    smtpObj.login(user=mail_user, password=mail_pass)
    smtpObj.sendmail(sender, receivers, msgObj.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as smtpMsg:
    print('邮件发送失败：', smtpMsg)
