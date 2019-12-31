# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-31 10:45:59
@LastEditTime : 2019-12-31 10:46:27
@Description: 缀点成线-简单  https://leetcode-cn.com/problems/check-if-it-is-a-straight-line
'''


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        gradient = lambda a,b: (b[1] - a[1])/(b[0]-a[0]) if a[0] != b[0] else None
        k = gradient(coordinates[0], coordinates[1])
        
        for i in range(1, len(coordinates) - 1):
            if k != gradient(coordinates[i], coordinates[i+1]):
                return False
        return True