# -*- coding:utf-8 _*-

"""
@Author: chenxj
@Time: 2019/4/19 15:02
@Mail: ccj799@gmail.com
@Description: 甲状腺项目no_filter替换fastq文件
"""

import re
import glob


def fq2raw(_file):
    thy = open(_file, 'r').readlines()
    raw = re.findall(r'in\d+ (.*?) --', thy[0])
    fq = re.findall(r'fq\d+ (.*?) --', thy[2])
    thy[2] = re.sub(fq[0], raw[0], thy[2])
    thy[2] = re.sub(fq[1], raw[1], thy[2])
    with open(_file, 'w') as f:
        for line in thy[2:]:
            print(line, end='', file=f)
    return


files = glob.glob('./01_reads_processing/*/*.sh')
for file in files:
    fq2raw(file)
    print(f"{file}替换完成")
