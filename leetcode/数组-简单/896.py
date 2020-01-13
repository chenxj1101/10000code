# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-04 10:29:48
@LastEditTime: 2019-12-04 10:31:25
@Description: 单调数列-简单  https://leetcode-cn.com/problems/monotonic-array/
'''


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A[-1] >= A[0]:
            for i in range(len(A)-1):
                if A[i+1] < A[i]:
                    return False
        elif A[-1] <= A[0]:
            for i in range(len(A)-1):
                if A[i+1] > A[i]:
                    return False
        return True

#---------------------------------------------------------------------------

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return (all(A[i] <= A[i+1] for i in range(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in range(len(A) - 1)))