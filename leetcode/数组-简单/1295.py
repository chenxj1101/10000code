# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2020-01-09 14:40:01
@LastEditTime : 2020-01-09 14:40:25
@Description: 统计位数为偶数的数字-简单  https://leetcode-cn.com/problems/find-numbers-with-even-number-of-digits
'''


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)