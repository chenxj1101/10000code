# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2020-01-09 14:35:52
@LastEditTime : 2020-01-09 14:36:23
@Description: 有序数组中出现次数超过25%的元素-简单  https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array
'''


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        flag, cnt =arr[0], 0
        for i in range(n):
            if arr[i] == flag:
                cnt += 1
                if cnt*4 > n:
                    return flag
            else:
                flag, cnt= arr[i], 1
