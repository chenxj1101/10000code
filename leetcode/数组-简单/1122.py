# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-11 10:50:06
@LastEditTime: 2019-12-11 10:50:27
@Description: 数组的相对排序-简单  https://leetcode-cn.com/problems/relative-sort-array
'''


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2 += sorted(set(arr1) - set(arr2))
        return sorted(arr1,key=arr2.index)