# -*- coding: utf-8 -*-

"""
20190103_1.py
工作代码，根据药物列表获取dailymed的数据
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

drug_info = {}
with open('./DM_XML/uniq_drug.list', 'r') as f:
    for line in f:
        line = line.strip()
        print(f"{line} start scrapy info")
        url = f"https://dailymed.nlm.nih.gov/dailymed/search.cfm?query={line}"
        res = requests.get(url)
        res.encoding = 'utf-8'
        html = res.text
        page = BeautifulSoup(html, 'lxml')

        label = page.h1.text.split(': ')[1].split('-')[0]

        ul = page.find('ul', class_='drug-information')
        lis = ul.find_all('li')

        codes = lis[0].text.strip().replace('\r\n', '').replace(' ', '')
        packager = lis[-1].text.split(": ")[1]

        time = page.find('p', class_='date').text.strip().replace('\r\n', '').replace(' ','').split('\t\t')[1]

        div = page.find('div', class_='drug-label-sections')
        info = div.ul.find_all('li')
        
        usage = ''
        descript = ''
        nct = ''

        for item in info:
            if item.a:
                if 'INDICATIONS AND USAGE' in item.a.text:
                    usage = item
                if 'DESCRIPTION' in item.a.text:
                    descript = item
                if 'CLINICAL STUDIES' in item.a.text or 'CLINICAL EFFICACY' in item.a.text:
                    nct = item
        
        # h2s = [h2.text for h2 in usage.div.find_all('h2')]
        usage_info = {}
        if usage:
            divs = usage.div.find_all('div', class_='Section')
            h2_pre = line
            for div in divs:
                if div.h2:
                    h2 = div.h2.text
                    h2_pre = h2
                    p = [p.text for p in div.find_all('p')][1:]
                    usage_info[h2] = p
                else:
                    h2 = h2_pre
                    p = [p.text for p in div.find_all('p')][1:]
                    if h2 in usage_info.keys():
                        usage_info[h2] += p
                    else:
                        usage_info[h2] = p
        descript_info = ''
        if descript:
            descript_info = [p.text for p in descript.find_all('p')][1:]

        nct_info = ''
        if nct:
            tmp="".join([p.text for p in nct.find_all('p')])
            nct_info = [f"NCT{num}" for num in re.findall(r"NCT(\d+)", tmp)]

        drug_info = {
            'Drug': line,
            'Label': label,
            'NDC Code': codes,
            'Packager': packager,
            'Update': time,
            'INDICATIONS AND USAGE': usage_info,
            'DESCRIPTION': descript_info,
            'NCT code': nct_info
        }

        with open('./DM_XML/drug_info.csv', 'a', encoding='utf-8') as f:
            print(drug_info, file=f)
        
        print(f"{line} scapy complete")
