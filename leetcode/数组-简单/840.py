# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-29 14:06:25
@LastEditTime: 2019-11-29 15:34:17
@Description: 矩阵中的幻方-简单  https://leetcode-cn.com/problems/magic-squares-in-grid
'''

class Solution(object):
    def numMagicSquaresInside(self, grid):
        R, C = len(grid), len(grid[0])

        def magic(a,b,c,d,e,f,g,h,i):
            return (sorted([a,b,c,d,e,f,g,h,i]) == list(range(1, 10)) and
                (a+b+c == d+e+f == g+h+i == a+d+g ==
                 b+e+h == c+f+i == a+e+i == c+e+g == 15))

        ans = 0
        for r in range(R-2):
            for c in range(C-2):
                if grid[r+1][c+1] != 5: continue  # optional skip
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1
        return ans