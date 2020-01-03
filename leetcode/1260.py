# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2020-01-03 11:15:06
@LastEditTime : 2020-01-03 14:47:51
@Description: 二维网格迁移-简单  https://leetcode-cn.com/problems/shift-2d-grid/solution
'''


import numpy as np
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid = np.array(grid)
        size = grid.size
        k %= grid.size
        while k > 0:
            L = np.vstack((grid[-1, -1], grid[:-1, -1].reshape(grid.shape[0] - 1, 1)))
            R = grid[:, :-1]
            grid = np.hstack((L, R))
            k -= 1
        return grid
