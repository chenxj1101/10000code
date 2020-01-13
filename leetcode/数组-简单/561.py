# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-18 16:02:56
@LastEditTime: 2019-11-18 16:09:23
@Description: 数组拆分 I-简单  https://leetcode-cn.com/problems/array-partition-i/
'''

from typing import List

def arrayPairSum(nums: List[int]) -> int:
    ns = list(sorted(nums))
    tmp = 0
    for i in range(0,len(ns), 2):
        tmp += ns[i]
    return tmp


#---------------------------------------------------------------------------------

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


l = [1, 4, 3, 2]

print(arrayPairSum(l))