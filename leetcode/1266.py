# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2020-01-06 16:14:28
@LastEditTime : 2020-01-06 16:15:57
@Description: 访问所有点的最小距离-简单  https://leetcode-cn.com/problems/minimum-time-visiting-all-points
'''


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x0, x1 = points[0]
        ans = 0
        for i in range(1, len(points)):
            y0, y1 = points[i]
            ans += max(abs(x0 - y0), abs(x1 - y1))
            x0, x1 = points[i]
        return ans
