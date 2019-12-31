# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-31 10:38:54
@LastEditTime : 2019-12-31 10:39:23
@Description: 玩筹码-简单  https://leetcode-cn.com/problems/play-with-chips
'''


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even = 0
        for c in chips:
            if c&1==0:
                even+=1
        return min(even,len(chips)-even)