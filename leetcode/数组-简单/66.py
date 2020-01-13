# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-01 10:08:39
@LastEditTime: 2019-11-01 10:55:07
@Description: 加1-简单  https://leetcode-cn.com/problems/plus-one/
'''

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = str(int(''.join([str(i) for i in digits])) + 1)
        nums = [i for i in num]
        return nums