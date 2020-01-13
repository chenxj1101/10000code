# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-11-14 09:56:08
@LastEditTime: 2019-11-14 09:59:34
@Description: 第三大的数-简单  https://leetcode-cn.com/problems/third-maximum-number/
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = set(nums)
        if len(n) < 3:
            return max(n)
        else:
            return list(sorted(n, reverse=True))[2]

#------------------------------------------------------------

import math
def thirdMax(nums):
    # 因为时间复杂度为O(N), 所以只能一一判断
    r = [float("-inf"), float("-inf"), float("-inf")]
    for n in nums:
        # 重复的值, 无需判断
        if n in r:
            continue
        # 出现最大的值
        if n > r[0]:
            r = [n, r[0], r[1]]
        # 出现第二大的值
        elif n > r[1]:
            r = [r[0], n, r[1]]
        # 出现第三大的值
        elif n > r[2]:
            r[2] = n
    
    return r[0] if math.isinf(r[2]) else r[2]

