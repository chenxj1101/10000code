# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-19 09:32:01
@LastEditTime: 2019-11-19 09:32:30
@Description: 重塑矩阵-简单  https://leetcode-cn.com/problems/reshape-the-matrix/
'''

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums)*len(nums[0]) != r*c:
            return nums
        a = [i for j in nums for i in j]
        b = []
        for i in range(0,len(a), c):
            b.append(a[i:i+c])
        return b