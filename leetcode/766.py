# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-28 13:27:37
@LastEditTime: 2019-11-28 13:31:22
@Description: 托普利茨矩阵-简单  https://leetcode-cn.com/problems/toeplitz-matrix/
'''

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        s = matrix[0][1:]
        for u in matrix:
            if s == u[1:]:
                s = u[:-1]
            else:
                return False
        return True

# ------------------------------------------------------------------

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        group = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in group:
                    group[r-c] = val
                elif group[r-c] != val:
                    return False
        return True