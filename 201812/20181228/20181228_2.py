# -*- coding: utf-8 -*-
"""
20181228_1.py
leetcode-1
"""

class Solution(object):
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

S = Solution()
a = S.twoSum([2,4,5,6,8,5], 10)
print(a)