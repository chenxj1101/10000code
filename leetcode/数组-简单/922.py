# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-05 10:31:28
@LastEditTime: 2019-12-05 10:53:48
@Description: 按奇偶排序数组 II-简单  https://leetcode-cn.com/problems/sort-array-by-parity-ii
'''

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        if A == []: return []
        B = []
        C = []
        D = []
        for x in A:
            if x%2 == 0:
                B.append(x)
            else:
                C.append(x)
        
        for i in range(len(B)):
            D.append(B[i])
            D.append(C[i])
        return D

#------------------------------------------------------------
        j = 1
        for i in xrange(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A

