# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-09 09:40:05
@LastEditTime: 2019-01-09 14:57:33
@Description: 有道翻译爬虫 
'''

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests

header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


home = 'http://fanyi.youdao.com/'
driver = webdriver.Chrome(executable_path='E:\\code\\youdao_translate\\chromedriver')
driver.get(home)
input_data =  driver.find_element_by_id('inputOriginal')

def youdao(key_word):
    input_data.clear()
    input_data.send_keys(key_word)
    time.sleep(2)
    result = driver.find_element_by_id('transTarget')
    return result.text

def youdao_info(key_word):
    url = f'http://dict.youdao.com/search?q={key_word}&keyfrom=new-fanyi.smartResult'
    res = requests.get(url, headers=header)
    res.encoding = 'utf-8'
    html = res.text
    page = BeautifulSoup(html, 'lxml')
    word_cn = key_word
    if page.find('div', class_='title').span:
        word_cn = page.find('div', class_='title').span.text.strip()
    return word_cn

with open('./info_source.txt', 'r', encoding='utf-8') as f:
    for line in f:
        time.sleep(2)
        line = line.strip()
        if not line.startswith('药物'):
            lines = line.split('\t')
            drug = lines[0]
            description = lines[-2]
            usage = lines[-1]

            # if ' ' in drug:
            #     drug = drug.replace(' ', '%20')
            # drug_cn = youdao_info(drug)
            # print(drug_cn)
            # if description:
            #     des = eval(description)
            #     des_cn = []
            #     for item in des:
            #         item = item.strip().replace('\xa0', '')
            #         item_cn = youdao(item)
            #         des_cn.append(item_cn)
            #         print(item_cn)
            #     print('\n')
            #     with open('./desc_cn.txt', 'a', encoding='utf-8') as f:
            #         print(' '.join(des_cn), file=f)
            print(drug)
            if usage:
                usage = eval(usage)
                usage_cn = []
                for key,value in usage.items():
                    key = key.strip().replace('\xa0', '')
                    tmp = ''.join(value)
                    value = tmp.strip().replace('\xa0', '')
                    print(key)
                    print(value)
                    key_cn = youdao(key)
                    value_cn = youdao(value)
                    content = key_cn + ' : ' + value_cn
                    usage_cn.append(content)
                with open('./usage_cn.txt', 'a', encoding='utf-8') as f:
                    print('\t'.join(usage_cn), file=f)
                    