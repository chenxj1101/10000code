# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-25 10:25:25
@LastEditTime : 2019-12-25 10:41:24
@Description: 公交站间的距离-简单  https://leetcode-cn.com/problems/distance-between-bus-stops
'''


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sumdistance = sum(distance)
        res = 0
        if start > destination:
            start, destination = destination, start
        while start < destination:
            res += distance[start]
            start += 1
        return min(res, sumdistance-res)