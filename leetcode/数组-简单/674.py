# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-21 09:35:42
@LastEditTime: 2019-11-21 09:54:55
@Description: 最长连续递增子序列-简单  https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/
'''

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        n = 1
        a = 1
        i = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i+1]:
                n += 1
            else:
                a = max(n, a)
                n = 1
            i += 1
        return max(n, a)

#---------------------------------------------------------
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor + 1)
        return ans
    