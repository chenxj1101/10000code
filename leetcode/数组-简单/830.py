# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-28 13:47:40
@LastEditTime: 2019-11-28 13:55:51
@Description: 较大分组的位置-简单  https://leetcode-cn.com/problems/positions-of-large-groups
'''

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        S += '0'
        i, j = 0, 0
        l = []
        while j < len(S):
            if S[i] != S[j]:
                if j - i > 2:
                    l.append([i, j-1])
                i = j
            j += 1
        return l

# -----------------------------------------------------------------------

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans = []
        i = 0
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans