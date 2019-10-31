# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-10-31 14:04:45
@LastEditTime: 2019-10-31 14:07:37
@Description: 最大子序和-简单  https://leetcode-cn.com/problems/maximum-subarray/
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        pre = nums[0]
        res = pre
        for i in range(1, n):
            pre = max(nums[i], pre+nums[i])
            res = max(res, pre)
        return res