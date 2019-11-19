# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-19 10:37:01
@LastEditTime: 2019-11-19 10:43:39
@Description: 子数组最大平均数 I-简单  https://leetcode-cn.com/problems/maximum-average-subarray-i/
'''


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        r = _sum = sum(nums[0:k])
        for i in range(k, len(nums)):
            _sum += nums[i] - nums[i-k]
            r = max(r, _sum)
        return r/k
