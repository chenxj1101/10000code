# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-05 15:38:46
@LastEditTime: 2019-11-05 16:25:21
@Description: 求众数-简单  https://leetcode-cn.com/problems/majority-element/
'''
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


#-----------------------------------
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_p = Counter(nums)
        return max(nums_p.keys(), key=nums_p.get)

