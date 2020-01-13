# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-20 14:23:26
@LastEditTime: 2019-11-20 14:24:43
@Description: 非递减数列-简单  https://leetcode-cn.com/problems/non-decreasing-array/
'''


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = True
        nums += [10000, 0]
        for i in range(len(nums) - 2):
            if nums[i] > nums[i + 1]:
                if not flag:
                    return False
                if nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                flag = False
        return True