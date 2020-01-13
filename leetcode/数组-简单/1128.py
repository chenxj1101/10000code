# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-12-23 10:07:40
@LastEditTime : 2019-12-23 11:14:41
@Description: 等价多米诺骨牌对的数量-简单  https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/
'''

import collections
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        d = collections.defaultdict(int)
        for i,j in dominoes:
            num = i*10 + j if i < j else: j*10 + i 
            d[num] += 1
        
        for k in d.values():
            ans += int(k*(k-1)/2)
        return ans