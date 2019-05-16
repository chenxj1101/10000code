# -*- coding:utf-8 _*-

"""
@Author: chenxj
@Time: 2019/4/28 10:04
@Mail: ccj799@gmail.com
@Description: 
"""

import argparse
import os

PERL = '/home/galaxy/.plenv/shims/perl'
TEXT2EXCEL = '/mnt/analysis/tests/test_cyw/script/Text2Excel.pl'


class TERT(object):

    def __init__(self):
        pass

    @property
    def args(self):
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument('-i', '--original', dest='original_file',
                            metavar='originalfile', type=str, required=True,
                            help='no_filter all_sample.snv.anno.txt')
        parser.add_argument('-r', '--replace_path', dest='replace_path',
                            metavar='dirname', type=str, required=False,
                            help='替换文件所在目录')
        args = parser.parse_args()
        return args

    @property
    def get_tert(self):
        tert = {}
        with open(self.args.original_file, 'r') as f:
            for i, line in enumerate(f):
                if line.startswith('TERT'):
                    tert[i] = line
        return tert

    @staticmethod
    def chunks(iters, n):
        for i in range(0, len(iters), n):
            yield iters[i:i + n]

    def replace_all(self):
        _file = []
        tert = self.get_tert
        with open(f"{self.args.replace_path}/all_sample.snv.anno.txt", 'r') as f:
            for i,line in enumerate(f):
                if i in tert.keys():
                    _file.append(tert[i])
                else:
                    _file.append(line)

        with open(f"{self.args.replace_path}/all_sample.snv.anno.txt", 'w') as f:
            for item in _file:
                print(item, file=f, end='')
        cmd = f"{PERL} {TEXT2EXCEL} -i {self.args.replace_path}/all_sample.snv.anno.txt -o \
                {self.args.replace_path}/all_sample.snv.anno.xlsx"
        os.system(cmd)

    def replace_singl(self):
        with open(f"{self.args.replace_path}/all_sample.snv.anno.txt", 'r') as f:
            fs = list(f)
            for _item in self.chunks(fs, 22):
                sample = _item[1].strip()
                with open(f"{self.args.replace_path}/{sample}/{sample}.snv.anno.txt", 'w') as f1:
                    for line in _item[3:]:
                        print(line, file=f1, end='')

    def __call__(self, *args, **kwargs):
        self.replace_all()
        self.replace_singl()


if __name__ == '__main__':
    TERT()()



