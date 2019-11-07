# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-07 10:53:53
@LastEditTime: 2019-11-07 10:55:49
@Description: 存在重复元素 II-简单  https://leetcode-cn.com/problems/contains-duplicate-ii/
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        i = 0
        while i < len(nums):
            a = nums[i+1: i+1+k]
            if nums[i] in a:
                return True
            i += 1
        return False
