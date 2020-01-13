# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-10-31 14:01:02
@LastEditTime: 2019-10-31 14:07:28
@Description: 移除元素-简单  https://leetcode-cn.com/problems/remove-element/
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i