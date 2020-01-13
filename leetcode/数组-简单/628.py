# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-19 10:26:14
@LastEditTime: 2019-11-19 10:31:38
@Description: 三个数的最大乘积-简单  https://leetcode-cn.com/problems/maximum-product-of-three-numbers/
'''


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l = sorted(nums)
        return max(l[-3]*l[-2]*l[-1], l[0]*l[1]*l[-1])