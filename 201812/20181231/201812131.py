# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-06 17:50:20
@LastEditTime: 2019-01-06 19:25:58
@Description: 小说爬虫，补20181231
'''

from urllib import request
from bs4 import BeautifulSoup
import collections
import re
import os
import time
import sys
import types


class download(object):
    def __init__(self, target):
        self.__tartet_url = target
        self.__head = {'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'}
        

    def get_download_url(self):
        charter = re.compile(u'[第弟](.+)章', re.IGNORECASE)
        target_req = request.Request(url=self.__tartet_url, headers=self.__head)
        target_response = request.urlopen(target_req)
        target_html = target_response.read().decode('gbk', 'ignore')
        listmain_soup = BeautifulSoup(target_html, 'lxml')
        charters = listmain_soup.find_all('div', class_ = 'listmain')
        download_soup = BeautifulSoup(str(charters), 'lxml')
        novel_name = str(download_soup.dl.dt).split("》")[0][5:]
        flag_name = "《" + novel_name + "》" + "正文卷"
        numbers = (len(download_soup.dl.contents) - 1)/2 - 8
        download_dict = collections.OrderedDict()
        begin_flag = False
        numbers = 1
        for child in download_soup.dl.children:
            if child != '\n':
                if child.string == u"%s" % flag_name:
                    begin_flag = True
                if begin_flag == True and child.a != None:
                    download_url = "https://www.biqukan.com" + child.a.get('href')
                    download_name = child.string
                    names = str(download_name).split('章')
                    name = charter.findall(names[0] + '章')
                    if name:
                        download_dict['第' + str(numbers) + '章' + names[1]] = download_url
                        numbers += 1
        return novel_name + '.txt', numbers, download_dict


    def Downloader(self, url):
        download_req = request.Request(url=url, headers=self.__head)
        download_response = request.urlopen(download_req)
        download_html = download_response.read().decode('gbk', 'ignore')
        soup_texts = BeautifulSoup(download_html, 'lxml')
        texts = soup_texts.find_all(id='content', class_='showtxt')
        soup_text = BeautifulSoup(str(texts), 'lxml').div.text.replace('\xa0', '')
        return soup_text


    def Writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n\n')
            for each in text:
                if each == 'h':
                    write_flag = False
                if write_flag == True and each != ' ':
                    f.write(each)
                if write_flag == True and each == '\r':
                    f.write('\n')
            f.write('\n\n')


if __name__ == "__main__":
    target_url = str(input("请输入小说目录下载地址：\n"))
    
    d = download(target = target_url)
    name, numbers, url_dict = d.get_download_url()
    if name in os.listdir():
        os.remove(name)
    index = 1

    print(f"《{name[:-4]}》 下载中：")
    for key, value in url_dict.items():
        d.Writer(key, name, d.Downloader(value))
        sys.stdout.write(f"已下载{float(index/numbers):.3f}\r")
        sys.stdout.flush()
        index += 1

    print(f" 《{name[:-5]}》 下载完成！")

    

