# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-06 10:34:20
@LastEditTime: 2019-12-06 10:34:42
@Description: 有序数组的平方-简单  https://leetcode-cn.com/problems/squares-of-a-sorted-array/
'''


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(map(lambda x: x*x, A))