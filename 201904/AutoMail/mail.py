# -*- coding:utf-8 _*-

"""
@Author: chenxj
@Time: 2019/4/15 13:59
@Mail: chenxj5@dazd.cn
@Description: 读取home目录下的mail_config.py下的邮件配置，会自动填充需求单，并将该需求单所在目录下的所有excel文件作为附件发送.
"""

import sys
import os
import argparse

sys.path.append('/mnt/analysis/tests/test_chenxj/auto_run/scripts')
# sys.path.append(f'/bio01/home/{getpass.getuser()}')
home = os.environ['HOME']
sys.path.append(home)

if not os.path.exists(f"{home}/mail_config.py"):
    print("请在自己home目录下创建mail_config.py文件，格式如下:\n"
          "config = {\n"
          "         'sender':'xxxx@dazd.cn',# 发件人\n "
          "         'receiver': ['1111@dazd.cn', '2222@dazd.cn'], # 收件人列表\n "
          "         'cc': ['3333@dazd.cn', '4444@dazd.cn'], # 抄送人列表\n"
          "         'smtpserver': 'smtp.dazd.cn', # 邮箱服务地址\n"
          "         'password': 'xxxxxx', # 密码\n"
          "         'name': 'XXXXX' # 发件人姓名\n"
          "}")
    sys.exit(2)


from sendmail import SendMail
from formatxlsx import get_unpass, unpass_table, fill_control
from mail_config import config


class AutoMail(object):
    """
    读取home目录下的mail_config.py下的邮件配置，会自动填充需求单，并将该需求单所在目录下的所有excel文件作为附件发送.
    请在当前分析路径执行脚本，因为会将脚本执行路径作为分析路径填充到需求单
    home目录下mail_config.py配置写法，权限设置最好为600：
    config = {
            'sender': 'chenxj5@dazd.cn', #发件人地址
            'receiver': ['111111@qq.com', '222222@qq.com'], #收件人列表
            'cc': ['333333@163.com', '444444@163.com'], #抄送人列表
            'smtpserver': 'smtp.dazd.cn', #邮箱服务地址
            'password': 'xxxxxx', #密码
            'name': '陈相剑' #发件人姓名
    }

    Arguments:
    -- control_file: report.py生成的质控文件.
    -- demand_path: 需求单所在目录，会自动填充该目录下的需求单，并将所有excel文件作为附件发送.
    """

    def __init__(self):
        self.to = config['receiver']
        self.cc = config['cc']
        self.name = config['name']
        self.user = config['sender']
        self.host = config['smtpserver']
        self.passwd = config['password']
        self.mail = SendMail(self.host, self.user, self.passwd, self.name)

    @property
    def args(self):
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument('-c', '--control_file', dest='control_file',
                            metavar='filename', type=str, required=True,
                            help='report.py生成的质控文件.')
        parser.add_argument('-d', '--demand_path', dest='demand_path',
                            metavar='dirname', type=str, required=True,
                            help='需求单所在目录，会将该目录下所有excel文件作为附件发送.')
        args = parser.parse_args()
        return args

    @property
    def abspath(self):
        return os.getcwd()

    @property
    def pdata(self):
        return self.abspath.split('/')[-1]

    @property
    def ptype(self):
        return self.abspath.split('/')[-2]

    @property
    def unpass(self):
        return get_unpass(self.args.control_file)

    def __call__(self, *args, **kwargs):

        demand_path = self.args.demand_path
        files = [f"{demand_path}/{f}" for f in os.listdir(demand_path) if f.endswith('xlsx') and 'report' not in f]
        for file in files:
            print(file)
            if 'BRCA' in file:
                fill_control(file, self.unpass, col_samp='T', col_path='X', col_pass='Y')
            elif 'DMD' in file:
                fill_control(file, self.unpass, col_samp='S', col_path='W', col_pass='X')
            elif '诺禾' in file:
                fill_control(file, self.unpass, col_samp='J', col_path='N', col_pass='O')
            elif '祥音' in file:
                fill_control(file, self.unpass, col_samp='K', col_path='N', col_pass='O')
                fill_control(file, self.unpass, col_samp='J', col_path='N', col_pass='O')
            else:
                fill_control(file, self.unpass)

        if os.path.exists("./unpass.txt"):
            tb = unpass_table('./unpass.txt')
            print(tb)
            os.system(f'rm ./unpass.txt')
            content = (f'各位好: <br>附件是{self.ptype}&nbsp;{self.pdata}上机的样本生信质控报告，<span style="color:red;">不通过样本如下：</span> <br>'
                       f"{tb.get_html_string(format=True, border=True, hrules=1, vrules=1)}"
                       f"分析路径为 {self.abspath}<br>"
                       f"祝好! <br>"
                       f"---------------------- <br>"
                       f"{self.name} &nbsp;&nbsp; 生物信息部 <br>"
                       f"{self.user} <br>")

            # self.mail.send_attach_mail(self.to, self.cc, f"{self.ptype}  {self.pdata}质控报告", content, demand_path)

        else:
            content = (f'各位好: <br>'
                       f'附件是{self.ptype}&nbsp;{self.pdata}上机的样本生信质控报告，<span style="color:red">所有样本质控通过。</span><br>'
                       f"分析路径为 {self.abspath}<br>"
                       f"祝好!<br>"
                       f"----------------------<br>"
                       f"{self.name} &nbsp;&nbsp; 生物信息部<br>"
                       f"{self.user}<br>")
            # self.mail.send_attach_mail(self.to, self.cc, f"{self.ptype}  {self.pdata}质控报告", content, demand_path)


if __name__ == '__main__':
    AutoMail()()
