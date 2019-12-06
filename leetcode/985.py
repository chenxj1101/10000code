# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-06 10:55:28
@LastEditTime: 2019-12-06 10:56:13
@Description: 查询后的偶数和-简单  https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries
'''

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        S = sum(x for x in A if x%2 == 0)
        ans = []
        
        for x,k in queries:
            if A[k] % 2 == 0:
                S -= A[k]
            A[k] += x
            if A[k] % 2 == 0:
                S += A[k]
            ans.append(S)
        return ans
    
