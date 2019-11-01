# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-01 15:08:29
@LastEditTime: 2019-11-01 16:15:35
@Description: 买卖股票的最佳时机-简单  https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
'''

from typing import List

def maxProfit(prices: List[int]) -> int:
    min_p, max_p = prices[0], 0
    for i in range(len(prices)):
        min_p = min(min_p, prices[i])
        max_p = max(max_p, prices[i]-min_p)
    return max_p

#print(maxProfit([7,1,5,3,6,4]))
#------------------------------------------------------------------
def maxProfit2(prices: List[int]) -> int:
    temp = max_profit = 0
    for i in range(len(prices)-1):
        temp = max(0, prices[i+1]-prices[i]+temp)
        max_profit = max(max_profit, temp)
    return max_profit

print(maxProfit2([7,1,5,3,6,4]))