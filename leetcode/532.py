# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-18 10:47:21
@LastEditTime: 2019-11-18 10:47:58
@Description: 数组中的k-diff数对-简单  https://leetcode-cn.com/problems/k-diff-pairs-in-an-array/
'''

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0: return 0
        s = set()
        d = set()
        for i in nums:
            if i-k in s:
                d.add(i-k)
            if i+k in s:
                d.add(i)
            s.add(i)
        return len(d)