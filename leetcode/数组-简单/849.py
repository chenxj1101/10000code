# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-03 17:26:33
@LastEditTime: 2019-12-03 17:27:00
@Description: 到最近的人的最大距离-简单  https://leetcode-cn.com/problems/maximize-distance-to-closest-person
'''

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1)/2)

        return int(max(ans, seats.index(1), seats[::-1].index(1)))