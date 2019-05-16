# -*- coding:utf-8 _*-

"""
@Author: chenxj
@Time: 2019/4/23 10:09
@Mail: ccj799@gmail.com
@Description: 甲状腺后续注释
"""


import argparse
import os
import json
import gzip
import pandas as pd
from collections import OrderedDict

PYTHON = '/home/galaxy/.pyenv/shims/python'
ANNOTAION = '/mnt/analysis/tests/test_cyw/script/thyroid_annotation_modify.py'
ANNOTAION_dazd = '/mnt/analysis/tests/test_cyw/script/thyroid_annotation_modify_dazd.py'
dazd = '/mnt/analysis/tests/test_cyw/script/Thyroid_snv_fusion_dazd.pl'
PERL = '/home/galaxy/.plenv/shims/perl'
TEXT2EXCEL = '/mnt/analysis/tests/test_cyw/script/Text2Excel.pl'


class RawAnnotaion(object):

    def __init__(self):
        pass

    @property
    def args(self):
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument('-s', '--sample_file', dest='sample_file',
                            metavar='samplefile', type=str, required=True,
                            help='sample_info.txt')
        parser.add_argument('-p', '--project_path', dest='project_path',
                            metavar='dirname', type=str, required=False,
                            help='项目分析目录')
        args = parser.parse_args()
        return args

    @property
    def get_sample_list(self):
        with open(self.args.sample_file, 'r') as f:
            for line in f:
                if not line.startswith('sample'):
                    sample = line.strip().split('\t')[1]
                    yield sample

    @property
    def get_path(self):
        path = os.path.abspath(self.args.project_path)
        return path

    @property
    def get_suffix(self):
        suffix = self.get_path.split('/')[-1]
        return suffix

    def make_dir(self):
        if not os.path.exists(f"{self.get_path}/Thyroid_result_{self.get_suffix}"):
            os.mkdir(f"{self.get_path}/Thyroid_result_{self.get_suffix}")
            for item in self.get_sample_list:
                os.mkdir(f"{self.get_path}/Thyroid_result_{self.get_suffix}/{item}")
        else:
            print(f"{self.get_path}/Thyroid_result_{self.get_suffix}已存在")


class SNV(RawAnnotaion):

    def __call__(self, *args, **kwargs):
        self.make_dir()
        for item in self.get_sample_list:
            vcf = f"{self.get_path}/05_variant_annotation/{item}/{item}.cosmic.vcf"
            out = f"{self.get_path}/Thyroid_result_{self.get_suffix}/{item}/{item}.snv.anno.txt"
            bam = f"{self.get_path}/03_bam_processing/{item}/04_base_recal/{item}.recal.bam"
            cmd = f"{PYTHON} {ANNOTAION}  -i {vcf} -o {out} -b {bam}"
            os.system(cmd)
            # print(out)
            _item = '\\\\n' + item + '\\n'
            cmd1 = f"sed '1 i{_item}' {out} >> {self.get_path}/Thyroid_result_{self.get_suffix}/all_sample.snv.anno.txt"
            # print(cmd1)
            os.system(cmd1)
        cmd2 = f"{PERL} {TEXT2EXCEL} -i {self.get_path}/Thyroid_result_{self.get_suffix}/all_sample.snv.anno.txt "\
               f"-o {self.get_path}/Thyroid_result_{self.get_suffix}/all_sample.snv.anno.xlsx"
        print(cmd2)
        os.system(cmd2)


class Fusion(RawAnnotaion):

    @property
    def bases(self):
        base = OrderedDict()
        for item in self.get_sample_list:
            base[item] = OrderedDict()
            _file = f"{self.get_path}/01_reads_processing/{item}/{item}.stat.json"
            with open(_file, 'r') as f:
                info = json.load(f)
                base[item]['Sample'] = item
                base[item]['Before QC (base)'] = info['summary']['before_filtering']['total_bases']
                base[item]['After QC (base)'] = info['summary']['after_filtering']['total_bases']
        return base

    @property
    def coverage(self):
        info = OrderedDict()
        for item in self.get_sample_list:
            info[item] = OrderedDict()
            _file = f"{self.get_path}/03_bam_processing/{item}/02_fusion_stat/coverage.report"
            with open(_file, 'r') as f:
                for line in f:
                    if not line.startswith('#'):
                        title, value = line.strip().split('\t')
                        title = title.replace('Total', 'ALL_MAP_DATA')
                        info[item][title] = value
        return info

    def quality(self):
        _base = self.bases
        _info = self.coverage
        _all = OrderedDict()
        for item in self.get_sample_list:
            _all[item] = dict(_base[item], **_info[item])
        df = pd.DataFrame(_all).T
        columns = ['Sample',
                   'Before QC (base)',
                   'After QC (base)',
                   '[ALL_MAP_DATA] Raw Reads (All reads)',
                   '[ALL_MAP_DATA] Paired Reads',
                   '[ALL_MAP_DATA] Mapped Reads',
                   '[ALL_MAP_DATA] Fraction of Mapped Reads',
                   '[ALL_MAP_DATA] Read and mate paired',
                   '[ALL_MAP_DATA] Fraction of Read and mate paired',
                   '[Target] Target Reads',
                   '[Target] Fraction of Target Reads in all reads',
                   '[Target] Fraction of Target Reads in mapped reads',
                   '[Target] Average depth',
                   '[Target] Coverage (>=100x)']
        df.to_csv(f'{self.get_path}/Thyroid_result_{self.get_suffix}/fusion.quality.report.txt', index=False, sep='\t', columns=columns)
        df.to_excel(f'{self.get_path}/Thyroid_result_{self.get_suffix}/fusion.quality.report.xlsx', index=False, columns=columns)

    def fusionreport(self):
        for item in self.get_sample_list:
            _list = []
            _file = f"{self.get_path}/03_bam_processing/{item}/02_fusion_stat/region.tsv.gz"
            with gzip.open(_file, 'rt') as f:
                for line in f:
                    _list.append(line.strip())

            _lines = "*".join(sorted(_list))
            _lines = _lines.replace('ENST00000331817.5\t481', 'KRT7-1\t481').replace('ENST00000331817.5\t1101',
                                                                                     'KRT7-2\t1101').replace(
                'ENST00000229239.9', 'GAPDH-1').replace('COSF1218', 'PAX8-PPARG 9').replace('COSF1220',
                                                                                            'PAX8-PPARG 10').replace(
                'COSF1224', 'PAX8-PPARG 8').replace('COSF1225', 'PAX8-PPARG 7').replace('COSF1272',
                                                                                        'RET-CCDC6').replace('COSF1492',
                                                                                                             'RET-NCOA4')
            _fusion = f"{self.get_path}/Thyroid_result_{self.get_suffix}/{item}/{item}.fusion.txt"
            with open(_fusion, 'w') as f:
                for line in _lines.split('*'):
                    print(line, file=f)

            _item = '\\\\n' + item + '\\n'
            cmd1 = f"sed '1 i{_item}' {_fusion} >> {self.get_path}/Thyroid_result_{self.get_suffix}/fusion.report.tmp"
            os.system(cmd1)
        cm2 = f"cat {self.get_path}/Thyroid_result_{self.get_suffix}/fusion.quality.report.txt \
                     {self.get_path}/Thyroid_result_{self.get_suffix}/fusion.report.tmp > \
                     {self.get_path}/Thyroid_result_{self.get_suffix}/fusion.report.txt"
        os.system(cm2)
        cmd3 = f"{PERL} {TEXT2EXCEL} -i {self.get_path}/Thyroid_result_{self.get_suffix}/fusion.report.txt " \
            f"-o {self.get_path}/Thyroid_result_{self.get_suffix}/fusion.report.xlsx"
        os.system(cmd3)
        os.system(f"rm {self.get_path}/Thyroid_result_{self.get_suffix}/fusion.report.tmp")

    def publish(self):

        _depth = {}
        with open(f"{self.get_path}/Thyroid_result_{self.get_suffix}/fusion.quality.report.txt", 'r') as f:
            for line in f:
                line = line.strip()
                if not line.startswith('Sample'):
                    sample = line.split('\t')[0]
                    depth = line.split('\t')[5]
                    _depth[sample] = depth

        for item in self.get_sample_list:
            with open(f"{self.get_path}/Thyroid_result_{self.get_suffix}/{item}/{item}.fusion.txt", 'r') as f:
                for i, line in enumerate(f):
                    line = line.strip()
                    if not line.startswith('#') and i < 7:
                        pos = line.split('\t')[0]
                        avgdepth = line.split('\t')[3]
                        ratio = f"{float(avgdepth)/float(_depth[item]):.3f}"
                        label = 'False'
                        if float(ratio) > 0.01:
                            label = 'True'

                        elif float(avgdepth) > 100:
                            label = 'Suspect'
                        with open(f'{self.get_path}/Thyroid_result_{self.get_suffix}/PublishedFusions.txt', 'a') as f1:
                            print(f"{item}\t{pos}\t{ratio}\t{label}", file=f1)
        cmd = f"{PERL} {TEXT2EXCEL} -i {self.get_path}/Thyroid_result_{self.get_suffix}/PublishedFusions.txt -o \
                {self.get_path}/Thyroid_result_{self.get_suffix}/PublishedFusions.xlsx"
        os.system(cmd)

    def __call__(self, *args, **kwargs):
        if self.get_suffix != 'no_filter':
            self.make_dir()
            self.quality()
            self.fusionreport()
            self.publish()


class DAZD(RawAnnotaion):

    def make_dazd(self):
        if not os.path.exists(f"{self.get_path}/Thyroid_result_dazd"):
            os.mkdir(f"{self.get_path}/Thyroid_result_dazd")
            for item in self.get_sample_list:
                os.mkdir(f"{self.get_path}/Thyroid_result_dazd/{item}")
        else:
            print(f"{self.get_path}/Thyroid_result_dazd已存在")

    def fusion_dazd(self):
        _samplist = list(self.get_sample_list)
        samplist = ' '.join(_samplist)
        cmd = f'{PERL} {dazd} -p {self.get_path} -i sample_info.txt -s "{samplist}" -f "{samplist}" -d dazd'
        print(cmd)
        os.system(cmd)

    def __call__(self, *args, **kwargs):
        if self.get_suffix != 'no_filter':
            self.make_dazd()
            self.fusion_dazd()


if __name__ == '__main__':
    SNV()()
    Fusion()()
    DAZD()()
