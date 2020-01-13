# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-22 15:07:27
@LastEditTime: 2019-11-22 15:08:02
@Description: 寻找数组的中心索引-简单  https://leetcode-cn.com/problems/find-pivot-index/
'''


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        left_sum = 0
        for i,x in enumerate(nums):
            if left_sum == (S - left_sum -x):
                return i
            left_sum += x
        return -1