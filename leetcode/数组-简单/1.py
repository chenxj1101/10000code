# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-10-31 13:54:08
@LastEditTime: 2019-10-31 14:07:46
@Description: 两数之和-简单  https://leetcode-cn.com/problems/two-sum/
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], i]
            else:
                lookup[num] = i
                