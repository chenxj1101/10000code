# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-05 09:55:02
@LastEditTime: 2019-11-05 10:44:41
@Description: 买卖股票的最佳时机 II-简单  https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
'''


from typing import List

def maxProfit(prices: List[int]) -> int:
    max_p = 0
    for i in range(len(prices) - 1):
        if prices[i+1] > prices[i]:
            max_p = prices[i+1] - prices[i]
    return max_p

#---------------------------------------------

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1 
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1