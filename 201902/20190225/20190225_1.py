#!/usr/bin/env python
# coding=UTF-8
'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Description: baidu_result_spider
@Date: 2019-02-25 14:56:37
'''

import re
import requests
import random
import time
import pymysql


def find_keyword_web(cur):
    key_word_link={}
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    pattern_link = re.compile(r'<h3 class="t">.*?href="(.*?)"', re.S)
    pattern_next_page = re.compile(r'下一页', re.S)
    pattern_front_page = re.compile(r'上一页', re.S)
    pattern_page_num_firt = re.compile(r'id="page">(.*?)</p>', re.S)
    cur.execute("select * from KeyWords")
    fr = cur.fetchall()
    for line in fr:
        key = line[1]
        aim = line[2]
        id = line[0]
        key_word_link[id]={}
        print("aim: " + aim + "key: " + key)
        baseUrl = 'http://www.baidu.com/s'
        page = 1
        data = {'wd': aim, 'pn': str(page - 1) + '0', 'tn': 'baidurt', 'ie': 'utf-8', 'bsst': '1'}
        first_page = requests.get(baseUrl, params=data, headers=headers)
        next = Judge_next_page(first_page, pattern_next_page)
        front = Judge_front_page(first_page, pattern_front_page)
        page_num = Get_Page_Num(pattern_page_num_first, first_page, front, next)
        key_word_link[id][key] = Get_Result_pages(baseUrl, page_num, pattern_link, aim, headers)
    print(key_word_link)
    return key_word_link


def Judge_next_page(page, pattern_next_page):
    items = re.findall(pattern_next_page, page.text)
    if(len(items) == 0):
        return False
    else:
        return True


def Judge_front_page(page, pattern_front_page):
    items = re.findall(pattern_front_page, page.text)
    if(len(items) == 0):
        return False
    else:
        return True


def Get_Page_Num(pattern_page_num_first, page, front, next):
    aim = re.compile(r'href="(.*?)"', re.S)
    item = re.findall(pattern_page_num_first, page.text)
    str=item[0]
    result=re.findall(aim, str)
    length=len(result)
    if (front == True) and (next == True):
        length = length - 1
    if (length == 0):
        length = 1
    return length


def Get_Result_pages(baseUrl, page_num, pattern_link, aim, headers):
    result = {}
    result[aim] = []
    for i in range(page_num):
        data = {'wd': aim, 'pn': str(i) + '0', 'tn': 'baidurt', 'ie': 'utf-8', 'bsst': '1'}
        page = requests.get(baseUrl, params=data, headers=headers)
        items =  re.findall(pattern_link, page.text)
        result[aim] = result[aim] + items
        time.sleep(1)
    return result


def write_to_file(link, cur):
    for keyID, Other in link.items():
        for k, pages_v in Other.items():
            for w, links in pages_v.items():
                for link in links:
                    cur.execute('INSERT INTO KeywordsLinks(Link, KeyWordID) VALUES ("%s", "%d")' % (pymysql.escape_string(link), keyID))
                    cur.connection.commit()


def get_keyword_sentence(cur):
    cur.execute("select * from KeywordsLinks")
    results = cur.fetchall()
    for result in results:
        try:
            print(result)
            link = result[1]
            linkID = result[0]
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            }

            cur.execute("select Word from KeyWords, KeywordLinks where KeywordsLinks.KeyWordID= KeyWords.KeyWordID and KeywordsLinks.LinkID=(%d)" % int(LinkID))")
            keyword = (cur.fetchone())[0]
            pattern = re.compile(r'.{5, 20}' + keyword + r'.{5,20}', re.S)
            replace = re.compile(r'<.*?>')
            page = requests.get(link, headers=headers, timeout=1)
            page = replace.sub('', page.text)
            items = re.findall(pattern, page)
            con = ""
            for item in items:
                con += item

            print(linkID)
            print(len(con))
            cur.execute("""UPDATE KeywordsLinks SET Content="%s" WHERE LinkID=%d""" % (pymysql.escape_string(con), LinkID))
            cur.connection.commit()
            time.sleep(random.random())
        except Exception:
            pass

def delete_empty(cur):
    cur.execute("DELETE FROM KeywordsLinks WHERE Content=''")


if __name__ == "__main__":
    user = input("Please input your mysql user name:")
    password = input("Please input your mysql password:")
    conn = pymysql.connect(host='localhost', user=user, password=password, db='mysql', charset='utf8', port=3306)
    cur = conn.cursor()
    cur.execute("USE BaiduResult")

    key_word_link = find_keyword_web(cur)
    write_to_file(key_word_link, cur)
    get_keyword_sentence(cur)
    delete_empty(cur)
    cur.close()
    conn.close()