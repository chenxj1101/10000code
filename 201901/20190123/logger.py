# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-23 14:48:20
@LastEditTime: 2019-01-23 15:16:51
@Description: logger
'''

import os
import time
import logging

# 创建logger实例，如果参数为空则返回root logger
logger = logging.getLogger('aiotest')
logger.setLevel(logging.DEBUG)


# 创建Handler，输出日志到控制台和文件
formatter = logging.Formatter(
    '%(asctime)s - %(filename)s[line:%(lineno)d] - <%(threadName)s %(thread)d>' +
    '- <Process %(process)d> - %(levelname)s: %(message)s'
)

basedir = os.path.abspath(os.path.dirname(__file__))
log_dest = os.path.join(basedir, 'logs')
if not os.path.isdir(log_dest):
    os.mkdir(log_dest)
filename = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.log'
file_handler = logging.FileHandler(os.path.join(log_dest, filename))
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# 将handler添加到logger中

logger.addHandler(file_handler)
logger.addHandler(stream_handler)