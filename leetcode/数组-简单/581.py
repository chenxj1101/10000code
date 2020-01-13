# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-19 09:53:56
@LastEditTime: 2019-11-19 09:55:03
@Description: 最短无序连续子数组-简单  https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
'''


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = sorted(nums)
        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2 and s[p1] == nums[p1]:
            p1 += 1
        while p1 <= p2 and s[p2] == nums[p2]:
            p2 -= 1
        return p2 - p1 + 1