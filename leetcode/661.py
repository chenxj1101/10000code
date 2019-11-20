# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-20 09:48:10
@LastEditTime: 2019-11-20 10:31:09
@Description: 图片平滑器-简单  https://leetcode-cn.com/problems/image-smoother/
'''


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        R, C = len(M), len(M[0])
        ans = [[0]*C for _ in M]

        for r in xrange(R):
            for c in xrange(C):
                count = 0

                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] /= count
        return ans