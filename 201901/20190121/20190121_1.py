# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-21 15:30:13
@LastEditTime: 2019-01-21 15:31:22
@Description: 工作代码，复制结果
'''

samples = [file for file in os.listdir('./backup')]

for sample in samples:
    cmd1 = f'cp ./CNV/{sample}*.tsv ./backup_t/{sample}'
    cmd2 = f'cp ./Fusion/{sample}*.tsv ./backup_t/{sample}'
    cmd3 = f'cp ./SNV/{sample}*.tsv ./backup_t/{sample}'
    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)
