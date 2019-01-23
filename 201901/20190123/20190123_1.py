# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-23 14:10:14
@LastEditTime: 2019-01-23 17:21:07
@Description: AQI_spider
'''

import time
import pymongo
import re
import requests
from datetime import datetime, date, timedelta
from concurrent import futures
from bs4 import BeautifulSoup
from logger import logger


client = pymongo.MongoClient(host='localhost', port=27017)
db = client.aqi
collection = db.aqi


def get_response(v_date, page_num):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://datacenter.mep.gov.cn',
        'Referer': 'http://datacenter.mep.gov.cn/websjzx/report/list.vm',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    }

    data = {
        'V_DATE': v_date,
        'pageNum': page_num,
        'orderby': '',
        'ordertype': '',
        'xmlname': '1512478367400',
        'gisDataJson': '',
        'queryflag': 'close',
        'customquery': 'false',
        'isdesignpatterns': 'false',
        'roleType': 'CFCD2084',
        'permission': '0',
        'AREA': '',
        'inPageNo': 1
    }


    try:
        resp = requests.post('http://datacenter.mep.gov.cn/websjzx/report/list.vm', data, headers=headers)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        logger.error('HTTP Error: %s', errh)
        return
    except requests.exceptions.ConnectionError a errc:
        logger.error('Connecting Error: %s', errc)
        return
    except requests.exceptions.Timeout as errt:
        logger.error('Timeout Error: %s', errt)
        return
    except requests.exceptions.TooManyRedirects as errr:
        logger.error('Redirect Error: %s', errr)
        return
    except requests.exceptions.RequestException as err:
        logger.error('Else Error: %s', err)
        return

    return resp


def get_page_nums(resp):
    if re.match(r'.*?<div class="report_page_null">暂无数据', resp.text, re.S):
        return 0, 0

    m = re.match(r'.*?总记录数.*?(\d+).*?条.*?总页数.*?(\d+).*?</div>', resp.text, re.S)
    record_nums = int(m.group(1))
    page_nums = int(m.group(2))
    return record_nums, page_nums


def get_page_data(resp):
    soup = BeautifulSoup(resp.text, 'lxml')
    tr_tags = soup.find('table', {'class': 'report-table'}).find_all('tr')
    for tr_tag in tr_tags[1:]:
        yield {
            'city': tr_tag.find('td', {'colid': 3}).get_text(),
            'aqi': tr_tag.find('td', {'colid': 4}).get_text(),
            'contaminant': tr_tag.find('td', {'colid': 5}).get_text(),
            'date': tr_tag.find('td', {'colid': 6}).get_text(),
            'level': tr_tag.find('td', {'colid': 8}).get_text(),
        }


def get_one_day_date(date):
    time.sleep(1)
    resp = get_response(date, 1)
    record_nums, page_nums = get_page_nums(resp)

    if record_nums == 0:
        logger.info(f'Date [{date}] has no data')
        return

    if record_nums > 0:
        if collection.find({'date': date}).count() == record_nums:
            logger.info(f'Date [{date}] has all data exist in MongoDB, ignore download')
            return

    for page_num in range(1, page_nums + 1):
        logger.info('Get date [{date}] No.{page_num} page data')
        time.sleep(1)
        resp = get_response(date, page_num)
        for item in get_page_data(resp):
            if not collection.find_one(item):
                if collection.insert_one(item):
                    logger.debug(f'Successfully Saved [{item}] to MongoDB')
                else:
                    logger.debug(f'Error saving [{item}] to MongoDB')
            else:
                logger.debug(f'Record [{item}] has exist in MongoDB')


def date_range(start, stop, step):
    while start <stop:
        yield datetime.strftime(start, '%Y-%m-%d')
        start += step


def get_many_days_data():
    gen_dates = date_range(date(2018, 8, 1), date.today(), timedelta(days=1))

    workers = 10
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(get_one_day_date, gen_dates)
    
    return len(list(res))


if __name__ == "__main__":
    t0 = time.time()
    count = get_many_days_data()
    logger.info(f'Download {count} days AQI data in {time.time() - t0}')