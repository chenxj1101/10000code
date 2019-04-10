#!/usr/bin/env python
# coding=UTF-8

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Description: 最后发送
@Date: 2019-04-10 14:15:30
'''


import sys
import os
from formatxlsx import get_unpass, unpass_table, fill_control
from sendmail import SendMail
from settings import mail_config


control_file = sys.argv[1]
demand_path = sys.argv[2]

host = mail_config['smtpserver']
user = mail_config['sender']
passwd = mail_config['password']
name = mail_config['name']
to = mail_config['receiver']
cc = mail_config['cc']


unpass = get_unpass(control_file)

files = [f"{demand_path}/{f}" for f in os.listdir(demand_path) if f.endswith('xlsx') and 'report' not in f]
for file in files:
    if 'BRCA' in file:
        fill_control(file, unpass, col_samp='T', col_path='X', col_pass='Y')
    else:
        fill_control(file, unpass)

abspath = os.getcwd()
project = abspath.split('/')[-1]

mail = SendMail(host, user, passwd, name)

if os.path.exists(f"{demand_path}/unpass.txt"):
    tb = unpass_table(f"{demand_path}/unpass.txt")
    os.system(f"rm {demand_path}/unpass.txt")
    content = (f'各位好: <br>附件是{project}上机的样本生信质控报告，<span style="color:red;">不通过样本如下：</span> <br>'
               f"{tb.get_html_string() }"
               f"分析路径为 {abspath}<br>" 
               f"祝好! <br>"
               f"---------------------- <br>"
               f"{name} &nbsp;&nbsp; 生物信息部 <br>"
               f"{user} <br>")

    mail.send_attach_mail(to, cc, f"{project}质控报告", content, demand_path)

else:
    content = (f'各位好: <br>'
               f'附件是{project}上机的样本生信质控报告，<span style="color:red">所有样本质控通过。</span><br>'
               f"分析路径为 {abspath}<br>"  
               f"祝好!<br>"
               f"----------------------<br>"
               f"{name} &nbsp;&nbsp; 生物信息部<br>"
               f"{user}<br>")
    mail.send_attach_mail(to, cc, f"{project}质控报告", content, demand_path)