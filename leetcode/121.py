# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-01 15:08:29
@LastEditTime: 2019-11-01 15:21:39
@Description: 买卖股票的最佳时机-简单  https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
'''

from typing import List

def maxProfit(prices: List[int]) -> int:
    min_p, max_p = prices[0], 0
    for i in range(len(prices)):
        min_p = min(min_p, prices[i])
        max_p = max(max_p, prices[i]-min_p)
    return max_p

print(maxProfit([7,1,5,3,6,4]))
