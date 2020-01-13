# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2020-01-02 15:24:32
@LastEditTime : 2020-01-02 15:25:10
@Description: 奇数值单元格的数目-简单  https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix
'''


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        from numpy import zeros
        matrix = zeros((n, m))
        for i,j in indices:
            matrix[i,:] += 1
            matrix[:,j] += 1
        return len(matrix[matrix%2 == 1])
