# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-06 10:25:15
@LastEditTime: 2019-12-06 10:28:25
@Description: 有效的山脉数组-简单  https://leetcode-cn.com/problems/valid-mountain-array
'''

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3: return False
        max_index = A.index(max(A))
        if max_index in [0, len(A) - 1]:
            return False
    
        for i in range(max_index):
            if A[i] >= A[i+1]:
                return False
        for j in range(max_index, len(A)-1):
            if A[j] <= A[j+1]:
                return False
        return True

#--------------------------------------------------------
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1

