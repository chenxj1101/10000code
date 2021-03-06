#!/home/galaxy/.pyenv/shims/python
# -*- coding: utf-8 -*-

"""
@Author: chenxj
@Time: 2019/4/3 17:03
@Mail: chenxj5@dazd.cn
@Description: 邮件构造发送
"""

import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SendMail(object):
    # 构造函数
    def __init__(self, host, user, passwd, user_name):
        self.user = user
        self._from = f"{user_name} <{user}>"

        smtp = smtplib.SMTP()
        smtp.connect(host, 25)
        smtp.login(user, passwd)
        self._smtp = smtp

    # 发送文本邮件
    def send_text_mail(self, to, cc, sub, content):
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = Header(self._from, 'utf-8')
        msg['To'] = Header(';'.join(to), 'utf-8')
        msg['Cc'] = Header(';'.join(cc), 'utf-8')
        msg['Subject'] = Header(sub, 'utf-8')

        try:
            self._smtp.sendmail(self.user, to + cc, msg.as_string())
            print(f'{sub} 邮件发送成功')
            return True
        except Exception as e:
            print(str(e))
            return False

    # 发送带附件邮件
    def send_attach_mail(self, to, cc, sub, content, path):
        amsg = MIMEMultipart()
        files = [path + '/' + f for f in os.listdir(path) if 'xlsx' in f]
        for file in files:
            filename = file.split("/")[-1]
            # print(filename)
            att = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', filename))
            amsg.attach(att)

        amsg.attach(MIMEText(content, 'HTML', 'utf-8'))
        amsg['From'] = Header(self._from, 'utf-8')
        amsg['To'] = Header(';'.join(to), 'utf-8')
        amsg['Cc'] = Header(';'.join(cc), 'utf-8')
        amsg['Subject'] = Header(sub, 'utf-8')

        try:
            self._smtp.sendmail(self.user, to + cc, amsg.as_string())
            print(f'{sub} 邮件发送成功')
            return True
        except Exception as e:
            print(str(e))
            return False

    # 析构函数
    def __del__(self):
        self._smtp.quit()
        self._smtp.close()


if __name__ == '__main__':
    host = 'smtp.dazd.cn'
    user = 'chenxj5@dazd.cn'
    passwd = 'xxxxxx'
    name = '陈相剑'

    sub = '质控报告'
    content = '各位好:\n 这是XXXXX上机的生信质控报告，请查收。'
    to = ['442185473@qq.com', '1483850264@qq.com']
    cc = ['chenxj799@163.com', 'cxjlg1@163.com']
    path = '/mnt/analysis/tests/test_chenxj/2019-04-09'

    mail = SendMail(host, user, passwd, name)
    mail.send_attach_mail(to, cc, sub, content, path)