# -*- coding: utf-8 -*-
"""
20181227-1.py
工作代码
"""
ann = {}
with open("./hotspot_v2_24k.xls", 'r') as f:
    for line in f:
        lines = line.strip().split('\t')
        gene = lines[0]
        pos = lines[1]
        ref = lines[4].split(':')[0]
        alt = lines[8].split(':')[0]
        pann = ''
        if 'splice' in pos:
            pann = f"p.{pos}"
        else:
            pann = f"p.{ref}{pos}{alt}"
        key = f"{gene}_{pann}"
        ann[key] = 1


with open("./hotspots_v2_recovered.xls", 'r') as f:
    for line in f:
        lines = line.strip().split('\t')
        gene = lines[0]
        indel = lines[9].split(':')[0]
        pann = f"p.{indel}"
        key = f"{gene}_{pann}"
        ann[key] = 1

with open("./CancerHotspots_clean_20181227.tsv", 'r') as f:
    for line in f:
        lines = line.split('\t')
        gene = lines[10]
        pann = lines[24]
        ann_type = lines[30]
        key = f"{gene}_{pann}"
        print(key ,ann_type)
        if key in ann.keys() or ('stop_gained' in ann_type and 'inframe' in ann_type):
            with open('./cancerhotspots_true.tsv', 'a') as f:
                print(line, file=f, end='')
        else:
            with open('./cancerhotspots_false.tsv', 'a') as f:
                print(line, file=f, end='')