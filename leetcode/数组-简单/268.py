# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-07 11:16:30
@LastEditTime: 2019-11-07 11:20:51
@Description: 缺失数字-简单  https://leetcode-cn.com/problems/missing-number/
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = set(nums)
        for i in range(len(nums)+1):
            if i not in a:
                return i

#-----------------------------------------------------------------------

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
