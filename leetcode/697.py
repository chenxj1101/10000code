# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-21 10:37:48
@LastEditTime: 2019-11-21 11:06:38
@Description: 数组的度-简单  https://leetcode-cn.com/problems/degree-of-an-array/
'''

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        
        ans = 0
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(right[x] - left[x] + 1)
        return ans