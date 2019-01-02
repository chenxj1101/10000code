# -*- coding: utf-8 -*-
"""
20190102_1.py
工作脚本
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

disease_all = []
headers = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1' }
with open('./my_cancer_genome_spider/variants.list', 'r') as f:
    for line in f:
        detail = {}
        url = line.strip()
        print(f"{url} start scrapy")
        # gene = url.split('/')[-2].upper()
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        html = res.text
        page = BeautifulSoup(html, 'lxml')

        div = page.find('div', class_='section-content active') 
        li = page.find('li',class_='menu_li')

        table = {}
        tds = div.table.find_all('td')
        info = [td.text.strip().replace('\xa0','') for td in tds if 'Pathway' not in td.text]
        for i in range(0,len(info), 2):
            table[info[i]] = info[i+1]

        disease = li.text.strip()
        gene = div.h2.string.split(' ')[0]
        cann = ''
        pann = ''
        if 'in' in div.h2.string:
            variant = div.h2.string.split(' in ')[0]
            if 'c.' in variant:
                cann = variant.split(' ')[1]
                pann = variant.split(' ')[2][1:-1]
            else:
                cann = " ".join(variant.split(' ')[1:])
        else:
            cann = ' '.join(div.h2.string.split(' ')[1:])

                
        

        description = []
        pmid = []

        if div.div:
            p = div.div.find_all('p')
            for item in p:
                description.append(item.text)
                pmid += re.findall(r'a href="(.*?)"', str(item))
        else:
            p = div.find_all('p')[:-3]
            for item in p:
                description.append(item.text)
                pmid += re.findall(r'a href="(.*?)"', str(item))


        time = div.find_all('p')[-1]
        modify = time.text.strip().split(': ')[1]

        detail = {
            'Gene':gene,
            'HGVS_C': cann,
            'HGVS_P': pann,
            'Disease': disease,
            'Info': table,
            'Description':description,
            'PMID':pmid,
            'Last Update':modify
        }

        with open('./my_cancer_genome_spider/variant_tmp.csv', 'a', encoding='utf-8') as f1:
            print(detail, file=f1)
        disease_all.append(detail)
        print(f"{url} scrapy complete")


# df = pd.DataFrame(gene_all)

# df.to_csv('./my_cancer_genome_spider/gene_info.csv', encoding='utf-8', index=False)