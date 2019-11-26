# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-26 10:14:51
@LastEditTime: 2019-11-26 10:15:45
@Description: 使用最小花费爬楼梯-简单  https://leetcode-cn.com/problems/min-cost-climbing-stairs/
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p1 = 0
        p2 = 0
        for i in range(2, len(cost) + 1):
            p1, p2 = p2, min(p2 + cost[i-1], p1 + cost[i-2])
        return p2
