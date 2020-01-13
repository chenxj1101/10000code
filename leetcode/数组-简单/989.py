# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-09 15:04:27
@LastEditTime: 2019-12-09 15:05:16
@Description: 数组形式的整数加法-简单  https://leetcode-cn.com/problems/add-to-array-form-of-integer/
'''

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return list(map(int, str(int(''.join(map(str, A)))+K)))


#-------------------------------------

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = list(map(int, str(carry))) + A
        return A