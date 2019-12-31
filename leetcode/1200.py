# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-31 10:20:08
@LastEditTime : 2019-12-31 10:20:42
@Description: 最小绝对差-简单  https://leetcode-cn.com/problems/minimum-absolute-difference
'''


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr2 = sorted(arr)
        min_v = 99999
        minus = {}
        for i in range(len(arr)-1):
            minus_v = arr2[i+1]-arr2[i]
            if minus_v not in minus.keys():
                minus[minus_v] = [[arr2[i], arr2[i+1]]]
            else:
                minus[minus_v].append([arr2[i], arr2[i+1]])
            min_v = min(min_v, arr2[i+1]-arr2[i])
        return minus[min_v]