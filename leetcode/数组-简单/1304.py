# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2020-01-09 15:00:12
@LastEditTime : 2020-01-09 15:00:57
@Description: 和为零的N个唯一整数-简单  https://leetcode-cn.com/problems/find-n-unique-integers-sum-up-to-zero
'''

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [x for x in range(n - 1)]
        ans.append(-sum(ans))
        return ans

######################################################################

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(1-n, n, 2))