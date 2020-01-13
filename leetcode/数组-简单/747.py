# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-26 10:36:37
@LastEditTime: 2019-11-26 10:38:48
@Description: 至少是其他数字两倍的最大数-简单  https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/
'''


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        if all(m >= 2*x for x in nums if x != m):
            return nums.index(m)
        else:
            return -1