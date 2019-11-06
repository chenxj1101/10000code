# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-06 13:39:10
@LastEditTime: 2019-11-06 13:39:40
@Description: 存在重复元素-简单  https://leetcode-cn.com/problems/contains-duplicate/
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        else:
            return False