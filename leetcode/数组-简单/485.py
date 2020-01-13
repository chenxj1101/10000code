# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-14 10:47:13
@LastEditTime: 2019-11-14 10:48:39
@Description: 最大连续1的个数-简单  https://leetcode-cn.com/problems/max-consecutive-ones/
'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = 0
        m = 0
        for num in nums:
            if num == 1:
                n += 1
                m = max(m, n)
            else:
                n = 0
        return m

#------------------------------------------------------------

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(len (substr) for substr in ''.join([str(x) for x in nums]).split("0"))