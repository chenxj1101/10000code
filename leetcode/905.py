# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-05 10:00:07
@LastEditTime: 2019-12-05 10:02:51
@Description: 按奇偶排序数组-简单  https://leetcode-cn.com/problems/sort-array-by-parity
'''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x%2)

#----------------------------------------------------------

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if A == []: return []
        B = []
        C = []
        for x in A:
            if x % 2 == 0:
                B.append(x)
            else:
                C.append(x)
        B.extend(C)
        return B
