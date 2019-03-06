#!/usr/bin/env python
# coding=UTF-8
'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Description: 单元测试
@Date: 2019-03-06 15:24:37
'''


from proxyPool.spiders.xiciSpider import XiciSpider

def case():
    proxy_list = XiciSpider.get_proxies()
    print(proxy_list)

case()